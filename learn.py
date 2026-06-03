def fibonacci(n):
	"""Generator yielding the first n Fibonacci numbers (0-indexed).

	Examples:
		list(fibonacci(0)) -> []
		list(fibonacci(1)) -> [0]
		list(fibonacci(5)) -> [0, 1, 1, 2, 3]
	"""
	a, b = 0, 1
	for _ in range(n):
		yield a
		a, b = b, a + b


if __name__ == "__main__":
	name = "Aadvi"
	print(f"Hiii!! {name}")
	# demo: print first 10 Fibonacci numbers
	print(list(fibonacci(10)))