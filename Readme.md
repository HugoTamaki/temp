```
exec(open("./Customer.py").read())
exec(open("./Item.py").read())
exec(open("./AbstractItem.py").read())
exec(open("./Dvd.py").read())

john = Customer("John Doe")
dvd = Dvd("A fuga", "Ação", "1")

john.getBalance()
// 0

john.rentItem(dvd, datetime.datetime.now())

john.getBalance()
// 350

dvd.rented
// True

john.bringBackItem("1", datetime.datetime.now() + datetime.timedelta(days=10))

dvd.rented
// False

john.getBalance()
// 850
```