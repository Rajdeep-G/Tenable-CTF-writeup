Refer to the writeup of spring_mvc_1

In MainController.java we have the function:-

```java
@PostMapping(path = "/main", consumes = "application/json")
	public String postMainJson(Model model) {
                model.addAttribute("flag", flags.getFlag("spring_mvc_4"));	// post main flag json
                return "flag";
        }
```

We have attribute **consumes** = **application/json**. Hence on adding the following header while making a post request to /main we will get our flag:-

>Content-Type: application/json

## flag{flag4_695954}