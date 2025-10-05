from pyscript import display, document



def create_order(e):
    document.getElementById('output').innerHTML = ""

    total = 0

    if document.getElementById("waffles").checked:
        total += int(document.getElementById("waffles").value)
    if document.getElementById("pancakes").checked:
        total += int(document.getElementById("pancakes").value)
    if document.getElementById("hashbrowns").checked:
        total += int(document.getElementById("hashbrowns").value)
    if document.getElementById("chicken_waffles").checked:
        total += int(document.getElementById("chicken_waffles").value)
    if document.getElementById("orange_juice").checked:
        total += int(document.getElementById("orange_juice").value)
    if document.getElementById("black_coffee").checked:
        total += int(document.getElementById("black_coffee").value)

    name = document.getElementById("name").value
    address = document.getElementById("address").value
    contact = document.getElementById("contact").value

    display(f"Order for: {name}", target="output")
    display(f"Address: {address}", target="output")
    display(f"Contact number: {contact}", target="output")
    display(f"Total: ₱{total:.2f}", target="output")
