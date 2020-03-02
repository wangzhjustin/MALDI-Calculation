import itertools
import json


class MolecularWeight:

    def __init__(self):
        filename = raw_input("Enter filename: ")
        if filename:
            datastore = self.load_file(filename)
        else:
            datastore = self.load_file("default_dataset.json")
        self.monomer_weight = datastore["monomer_weight"]
        self.monomer_weight_keys = self.monomer_weight.keys()
        self.polymer_weight = datastore["polymer_weight"]
        self.range_bottom = datastore["range_bottom"]
        self.range_top = datastore["range_top"]
        self.error_number = datastore["error_number"]
        self.main()

    def load_file(self, filename):
        with open(filename, 'r') as f:
            datastore = json.load(f)
            return datastore

    def check_list(self, number, final_alpha):
        result = {}
        for monomer_weight_num in self.polymer_weight:
            if abs(monomer_weight_num - number) < self.error_number:
                result[number] = final_alpha
                return result
            else:
                pass

    def use_iter(self, range_num):
        product_list = list(itertools.product(self.monomer_weight_keys, repeat=range_num))
        return product_list

    def combinations_generator(self):
        steps = []
        for range_num in range(self.range_bottom, self.range_top):
            step = self.use_iter(range_num)
            steps.extend(step)
        return steps

    def result_calculator(self, combination):
        final_value = 0
        final_alpha = ""
        for item in combination:
            value = self.monomer_weight[item]
            final_value += value
            final_alpha += item
        result = self.check_list(final_value, final_alpha)
        return result

    def main(self):
        results = []
        combinations = self.combinations_generator()
        for combination in combinations:
            result = self.result_calculator(combination)
            if result:
                results.append(result)
        print (results)


MolecularWeight()