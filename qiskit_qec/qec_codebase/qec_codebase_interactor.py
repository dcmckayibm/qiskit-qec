import pathlib, os, json
from qiskit_qec.codes.subsystemcodes import SubSystemCode

from qiskit_qec.structures.gauge import GaugeGroup
from qiskit_qec.operators.pauli_list import PauliList
from typing import List, Dict


class QECCodeBase:
    parent_name = pathlib.Path(__file__).parent.resolve()
    codebase_name = "qec_codebase"
    codebase_path = os.path.join(parent_name, codebase_name)
    code_path_format = os.path.join("n_length_{}_codes", "codes_n_{}_k_{}.json")  # n,n,k"

    def __init__(self):
        pass

    def get_subsystem_code(self, n_len, k_dim, **additional_params) -> List[SubSystemCode]:

        qec_code_jsons = self._load_code_jsons_from_n_k(n_len, k_dim)
        if len(additional_params) > 0:
            print(
                f"WARNING. You have {len(additional_params)} additional params. Additional params may cause really slow results"
            )
            qec_code_jsons = self._additional_param_query(qec_code_jsons, **additional_params)

        qec_code_list = self._convert_json_to_subsystem_codes(qec_code_jsons)
        return qec_code_list

    def _evaluate_codepath(self, n_len, k_dim):
        return os.path.join(self.codebase_path, self.code_path_format).format(n_len, n_len, k_dim)

    def _load_code_jsons_from_n_k(self, n_len, k_dim) -> Dict:
        code_path = self._evaluate_codepath(n_len, k_dim)
        with open(code_path, "r") as f:  # should except if invalid
            qec_code_jsons = json.load(f)
        return qec_code_jsons

    def _convert_json_to_subsystem_codes(self, qec_code_jsons):
        qec_code_list = []
        for cur_code_json in qec_code_jsons.values():
            a_gottesman_pauli = cur_code_json["gottesman_form"][0].upper()
            cur_code = SubSystemCode(
                GaugeGroup(PauliList(a_gottesman_pauli)), parameters=cur_code_json
            )
            qec_code_list.append(cur_code)
        return qec_code_list

    def _additional_param_query(self, json_codes, **additional_params):
        results = {}
        for k, cur_code_dict in json_codes.items():
            if self._is_valid(cur_code_dict, additional_params):
                results[k] = json_codes[cur_code_dict["uuid"]]

        return results

    def _is_valid(self, code_info_dict, additional_params):
        for param, value in additional_params.items():
            if not (code_info_dict[param] == value or value in code_info_dict[param]):
                return False
        return True
