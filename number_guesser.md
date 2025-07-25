### Why no `str()` needed in this `print()`?

```python
print("you got it in", guesses, "guesses")

```
#### Reason:
When you use commas in print(), Python automatically converts non-string types (like integers) into strings for you.

### 📍 In Frappe Python: Why `str()` is important

If you're using `frappe.msgprint()` or `print()` with `+`, you **must** convert numbers using `str()`.

```python
guesses = 3
# ✅ Correct ways
frappe.msgprint("You got it in " + str(guesses) + " guesses")
frappe.msgprint(f"You got it in {guesses} guesses")
frappe.msgprint("You got it in {} guesses".format(guesses))

# ❌ Incorrect
frappe.msgprint("You got it in " + guesses + " guesses")  # TypeError
```