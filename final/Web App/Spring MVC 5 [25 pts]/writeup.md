Refer to the writeup of spring_mvc_1

In MainController.java we have the function:-

```java
@RequestMapping(path = "/main", method = RequestMethod.OPTIONS)
        public String optionsMain(Model model) {
                model.addAttribute("flag", flags.getFlag("spring_mvc_5"));	// options main
                return "flag";
        }
```

We can clearly see that we need to make a **OPTIONS** request to /main.
From the response body we will directly get our flag:-

## flag{flag5_70102b}