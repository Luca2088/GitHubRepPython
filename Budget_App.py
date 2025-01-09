def title_line(name):
    title_name = name.__repr__()
    asteric_nu = 30 - len(title_name)
    asteric_side = asteric_nu//2
    return str(('*'*asteric_side)+title_name+("*"*asteric_side))

def display_ledger(name):
    main_ledger = name.ledger
    indexes_of_ledger = len(main_ledger)
    final_ledger = ''
    final_amount = 0
    for diction in range(indexes_of_ledger):
        description = main_ledger[diction]['description']
        amount = main_ledger[diction]['amount']
        final_amount += amount
        indexes_description = len(description)
        if indexes_description > 23:
            indexes_description = 23
        if type(amount) != float:
           amount = f'{amount}.00'
        indexes_amount = len(str(amount))
        if indexes_amount > 7:
           indexes_amount = 7
        spaces = ' '*((23-indexes_description)+(7-indexes_amount))
        str_description = description[:indexes_description] 
        str_amount = str((amount))[:indexes_amount]
        final_ledger += f'\n{str_description}{spaces}{str_amount}'
    return f'{final_ledger}\nTotal: {final_amount}'

class Category:
    #1__init__ , __repr() and __str__
    def __init__(self,name):
        self.name = name
        self.ledger = []

    def __repr__(self):
        return self.name 

    def __str__(self):
        final = title_line(self)+display_ledger(self)
        return str(final)

    #METHODS:
    def deposit(self,amount,description=''):
        deposit_ledger = {'amount':amount,'description':description}
        self.ledger.append(deposit_ledger)

    def get_balance(self):
        balance = 0
        list_of_dicts = self.ledger
        for dicts in range(len(list_of_dicts)):
            balance += list_of_dicts[dicts]['amount']
        return balance

    def check_funds(self,amount):
        balance = self.get_balance()
        return (amount <= balance)

    def withdraw(self,amount,description=''):
        if self.check_funds(amount)==True:
           withdraw_amount = -1*amount
           withdraw_ledger = {'amount':withdraw_amount,'description':description}
           self.ledger.append(withdraw_ledger)
           return True
        else:
            return False 
        
    def transfer(self,amount,category):
        transferee_message = f'Transfer to '+category.__repr__()
        transfered_message = f'Transfer from '+self.__repr__()
        if self.check_funds(amount)==True:
            self.withdraw(amount,transferee_message)
            category.deposit(amount,transfered_message)
            return True
        return False

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(400, 'groceries')
food.withdraw(150, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(10,'sweater')
print(food)
auto = Category('Auto')
auto.deposit(100)
auto.withdraw(10)

def percentage_calculator(categories):
    indexes_categories = len(categories)
    list_percentages = []
    for category in range(indexes_categories):
        main_ledger = (categories[category]).ledger
        indexes_of_ledger = len(main_ledger)
        spent_amount = 0
        received_amount = 0
        for diction in range(indexes_of_ledger):
            amount = main_ledger[diction]['amount']
            if amount<0:
                spent_amount += -1*(amount)
        received_amount = categories[category].get_balance()+(spent_amount)
        percentage =(abs(spent_amount / received_amount) *100)//10 
        list_percentages.append((categories[category],percentage))
        
    return (list_percentages)

def first_part(perc_index,percentages):
    first_part_line = ''
    for level in reversed(range(0,11)):
        line = ''
        for num in range(perc_index):
            if level <= percentages[num]:
                line += 'o  '
            else:
                line += '   '
        if level == 10:
            one_level = f'{level}0| {line}\n'
        elif level == 0:
            one_level = f'  {level}| {line}\n'
        else:
            one_level = f' {level}0| {line}\n'
        first_part_line += one_level
    return str(first_part_line)

def second_part(names,perc_index):
    second_part_line = ''
    dash_line = f'    -{"---"*perc_index}'
    second_part_line += dash_line
    max_index = 0
    for o in range(perc_index):
        name = names[o].__repr__()
        name_index = len(name)
        if name_index > max_index:
           max_index = name_index 
    letter_line = '     '
    for letter in range(max_index):
        line = f'\n{letter_line}'
        for name in names:
            word = name.__repr__()
            try:
                line += word[letter]+'  '
            except IndexError:
                line += '   '
        second_part_line += line
    return second_part_line

def graph_creator(list_of_tuples):
    final_line = 'Percentage spent by category\n'
    indexes = len(list_of_tuples)
    percentages = []
    names = []
    for i in range(indexes):
        percentages.append(list_of_tuples[i][1])
        names.append(list_of_tuples[i][0])
    perc_index = len(percentages)

    final_line += str(first_part(perc_index,percentages))
    final_line += str(second_part(names,perc_index))
    return final_line

def create_spend_chart(categories):
    return(graph_creator(percentage_calculator(categories)))


print(create_spend_chart([food,auto,clothing]))

def create_spend_chart(categories):
  spent_dict = {}
  for category in categories:
    total_category = 0 
    for j in category.ledger:
      if j['amount'] < 0 :
        total_category+= abs(j['amount'])
    spent_dict[category.name] = round(total_category,2)
  total = sum(spent_dict.values())
  percent_dict = {}
  for k in spent_dict.keys():
    percent_dict[k] = int(round(spent_dict[k]/total,2)*100)
  output = 'Percentage spent by category\n'
  for i in range(100,-10,-10):
    output += f'{i}'.rjust(3) + '| '
    for percent in percent_dict.values():
      if percent >= i:
        output+= 'o  '
      else:
        output+= '   '
    output += '\n' 
  output += ' '*4+'-'*(len(percent_dict.values())*3+1)
  output += '\n     '
  dict_key_list = list(percent_dict.keys())
  max_len_category = max([len(i) for i in dict_key_list])
  
  for i in range(max_len_category):
    
    for name in dict_key_list:
      if len(name)>i:
        output+= name[i] +'  '
      else:
        output+= '   '
    if i < max_len_category-1:
      output+='\n     '
    
  return output
