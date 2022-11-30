from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

# Set the app size
Window.size = (500,700)

# Designate Our .kv design file 
Builder.load_file('calc.kv')

class MyLayout(Widget):
	def clear(self):
		self.ids.calc_input.text = '0'

	# Create a button pressing function
	def button_press(self, button):
		# create a variable that contains whatever was in the text box already
		prior = self.ids.calc_input.text
		
		# determine if 0 is sitting there
		if prior == "0":
				self.ids.calc_input.text = ''
				self.ids.calc_input.text = f'{button}'
		else: 
			self.ids.calc_input.text = f'{prior}{button}'

	# create addition function
	def add(self):
		# create a variable that contains whatever was in the text box already
		prior = self.ids.calc_input.text
		
		# slap a plus sign to the text box
		self.ids.calc_input.text = f'{prior}+'

	# create substraction function
	def subtract(self):
		# create a variable that contains whatever was in the text box already
		prior = self.ids.calc_input.text
		
		# slap a substract sign to the text box
		self.ids.calc_input.text = f'{prior}-'

	# create multiplication function
	def multiply(self):
		# create a variable that contains whatever was in the text box already
		prior = self.ids.calc_input.text
		
		# slap a multiplication sign to the text box
		self.ids.calc_input.text = f'{prior}*'

	# create divide function
	def divide(self):
		# create a variable that contains whatever was in the text box already
		prior = self.ids.calc_input.text
		
		# slap a divide sign to the text box
		self.ids.calc_input.text = f'{prior}/'

	def percent(self):
		# create a variable that contains whatever was in the text box already
		prior = self.ids.calc_input.text

		# slap a percentage sign to the text box
		self.ids.calc_input.text = f'{prior}%'



	# create equals to function
	def equals(self):
		prior = self.ids.calc_input.text

		# Addition
		if "+" in prior:
			num_list = prior.split("+")
			answer = 0
			# loop thru our list
			for number in num_list:
				if number.isdigit():
					answer = answer + int(number)
				else: 
					answer = answer + float(number)	

			# print the answer in the text box
			self.ids.calc_input.text = str(answer)	


	    # Substraction		
		elif "-" in prior:
			num_list = prior.split("-")
			answer = 0
			if num_list[0].isdigit():
				prev = int(num_list[0])
			else:
				prev = float(num_list[0])	

			# loop thru our list
			for number in range(1,len(num_list)):
				if number == 1:
					if num_list[number].isdigit():
						answer = prev - int(num_list[number])
					else:
						answer = prev - float(num_list[number])	
				else:
					if num_list[number].isdigit():
						answer = answer - int(num_list[number])
					else:
						answer = answer - float(num_list[number])	


			if len(num_list) == 2:
				answer = float(num_list[0]) - float(num_list[1])
			

			# print the answer in the text box
			self.ids.calc_input.text = str(answer)		

		# Multiplication
		elif "*" in prior:
			num_list = prior.split("*")
			answer = 1
			
			# loop thru our list
			for number in num_list:
				if number.isdigit():
					answer = answer * int(number)
				else:
					answer = answer * float(number)	

			# print the answer in the text box
			self.ids.calc_input.text = str(answer)	


		#Division
		elif "/" in prior:
			num_list = prior.split("/")
			answer = 0
			prev = float(num_list[0])
			# loop thru our list
			for number in range(1,len(num_list)):
				if number == 1:
					answer = prev / float(num_list[number]) 
				else:
					answer = answer / float(num_list[number])	 

			# print the answer in the text box
			self.ids.calc_input.text = str(answer)	


		# percent
		elif "%" in prior:
			num_list = prior.split("%")
			answer = 0
			for number in range(1,len(num_list)):
				if number == 1:
					if num_list[number].isdigit():
						prev = int(num_list[number-1])/100
						answer = prev * int(num_list[number])
					else:
						prev = float(num_list[number-1])/100
						answer = prev * float(num_list[number])
								
				else:
					if num_list[number].isdigit():
						prev = 	answer / 100
						answer = prev * int(num_list[number])
					else:
						prev = 	answer / 100
						answer = prev * float(num_list[number])
							
			# print the answer in the text box
			self.ids.calc_input.text = str(answer)	



				

class CalculatorApp(App):
	def build(self):
		return MyLayout()

if __name__ == '__main__':
	CalculatorApp().run()

