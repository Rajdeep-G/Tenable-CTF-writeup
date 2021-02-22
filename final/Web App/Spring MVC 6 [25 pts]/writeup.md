Refer to the writeup of spring_mvc_1

In MainController.java we have the function:-

```java
@RequestMapping(path = "/main", method = RequestMethod.GET, headers = "Magic-Word=please")
        public String headersMain(Model model) {
                model.addAttribute("flag", flags.getFlag("spring_mvc_6"));	// headers main
                return "flag";
        }
```

We have **method = RequestMethod.GET** and **headers = "Magic-Word=please"**. So we need to make a get request to /main with a header set to:-
>Magic-Word: please

## Hurray you have the flag now!!

## flag{flag6_ca1ddf}