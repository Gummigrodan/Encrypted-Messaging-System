class Command:
    def __init__(self, number):
        self.number = number

    def use_command(self, array, undo):
        if undo == False:
            match self.number:
                case "1":
                    return self.command_one(array)
                case "2":
                    return self.command_two(array)
                case "3":
                    return self.command_three(array)
                case "4":
                    return self.command_four(array)
                case "5":
                    return self.command_five(array)
        else:
            match self.number:
                case "1":
                    return self.undo_one(array)
                case "2":
                    return self.undo_two(array)
                case "3":
                    return self.undo_three(array)
                case "4":
                    return self.undo_four(array)
                case "5":
                    return self.undo_five(array)

    def command_one(self, array):
        array.reverse()

        return array

    def undo_one(self, array):
        array.reverse()

        return array

    def command_two(self, array):
        item_to_swap = array[0]
        del array[0]
        array.append(item_to_swap)

        return array

    def undo_two(self, array):
        item_to_swap = array[len(array)-1]
        del array[len(array)-1]
        array.insert(0, item_to_swap)

        return array

    def command_three(self, array):
        for x in range(0, len(array)-1, 2):
            array[x], array[x+1] = array[x+1], array[x]

        return array

    def undo_three(self, array):
        for x in range(0, len(array)-1, 2):
            array[x], array[x+1] = array[x+1], array[x]
    
        return array

    def command_four(self, array):
        items_to_swap = array[:len(array)//2]
        del array[:len(array)//2]
        array.extend(items_to_swap)

        return array

    def undo_four(self, array):
        swap_index = len(array) - len(array) // 2
        items_to_swap = array[:swap_index]
        del array[:swap_index]
        array.extend(items_to_swap)

        return array

    def command_five(self, array):
        items_to_swap = []
        kept_items = []

        add_to_swap = False
        for item in array:
            if add_to_swap:
                items_to_swap.append(item)
                add_to_swap = False
            else:
                kept_items.append(item)
                add_to_swap = True

        array[:] = items_to_swap + kept_items

        return array

    def undo_five(self, array):
        mid = len(array) // 2
        items_to_swap = array[:mid]
        kept_items = array[mid:]

        original = []
        for i in range(len(kept_items)):
            original.append(kept_items[i])
            if i < len(items_to_swap):
                original.append(items_to_swap[i])

        array[:] = original

        return array