class Country:
    name = ""

    def __str__(self):
        return "Hello from {}".format(self.name)


c = Country()
print(c)
