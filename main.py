import itertools
import json


class MolecularWeight:

    def __init__(self):
        filename = input("Enter filename: ")
        if filename:
            datastore = self.load_file(filename)
        else:
            datastore = self.load_file("default_dataset.json")
        self.monomer_weight = datastore["monomer_weight"]
        self.monomer_charge = datastore["monomer_charge"]
        self.polymer_charge = datastore["polymer_charge"]
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

    def check_list(self, number, final_alpha, final_charge):
        result = {}
        for monomer_weight_num in self.polymer_weight:
            if abs(monomer_weight_num - number) < self.error_number and final_charge in self.polymer_charge:
                result[round(number, 2)] = (final_alpha, final_charge)
                return result
            else:
                pass

    def use_iter(self, range_num):
        product_list = list(itertools.combinations_with_replacement(self.monomer_weight_keys, range_num))
        return product_list

    def combinations_generator(self):
        steps = []
        for range_num in range(self.range_bottom, self.range_top):
            step = self.use_iter(range_num)
            steps.extend(step)
        return steps

    def result_calculator(self, combination):
        final_value = 0
        final_charge = 0
        final_alpha = ""
        for item in combination:
            value = self.monomer_weight[item]
            final_value += value
            final_charge += self.monomer_charge[item]
            final_alpha += item
        result = self.check_list(final_value, final_alpha, final_charge)
        return result

    def main(self):
        combinations = self.combinations_generator()
        for combination in combinations:
            result = self.result_calculator(combination)
            if result:
                print(result)


MolecularWeight()
