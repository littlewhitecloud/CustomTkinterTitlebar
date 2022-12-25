### Update log~
#### Verison:1.0.5
> - Add custom showing maxsize minsize
>> - Like this:
>>> ![image](https://user-images.githubusercontent.com/71159641/209436383-6099be9f-49bd-467a-97c0-2158fda329a6.png)
>> - Or this:
>>> ![image](https://user-images.githubusercontent.com/71159641/209436402-d998d26f-e076-46be-bf9e-06733dc4f659.png)
>> - You can use function usemaxmin() to decide what to how
>>> - About the function
>>> - Args usemaxmin(self, minsize:bool, maxsize:bool, minshow:bool, maxshow:bool)
```
from custom import Tk
example = Tk()
example.usemaxmin(False, False, False, False) # only show close button
example.mainloop()
```
