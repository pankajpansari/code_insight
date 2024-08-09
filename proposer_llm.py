import os
import pathlib

import base_llm
import utils

class ProposerLLM(base_llm.BaseLLM):
    def __init__(self, model, parameter):
        super().__init__(model, parameter)
        self.parameter_prompt_path = f"{parameter['prompt_file']}"
        self.system_prompt_path = f"{utils.CONFIG['proposers']['system_prompt']}"
        output_prefix = utils.CONFIG['assignment']['problem_file'].split('/')[1].split('.')[0]  
        self.output_path = utils.CONFIG['assignment']['intermediate_path']
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)
        self.output_filename = (
            f"{output_prefix}_proposer_{model['type']}"
            f"_{parameter['name']}.txt"
        )

    def create_message_content(self) -> str:
        problem_statement = self.read_file(self.problem_path)
        program_solution = self.read_file(self.solution_path)
        parameter_prompt = self.read_file(self.parameter_prompt_path)

        return (f"<problem> {problem_statement} </problem> \n\n"
                f"<code> {program_solution} </code> \n\n"
                f"<instructions> {parameter_prompt} </instructions>")