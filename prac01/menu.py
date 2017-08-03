name = input("Enter name: ")
print("(H)ello\n(G)oodbye\n(Q)uit\n")
choice = input("\n>>>").upper()
while choice != "Q":
    if choice == "H":
        print("Hello",name)
    elif choice == "G":
        print("Goodbye",name)
    else:
        print("Invalid choice")
    print("(H)ello\n(G)oodbye\n(Q)uit\n")
    choice = input("\n>>>").upper()
print("Finished.")