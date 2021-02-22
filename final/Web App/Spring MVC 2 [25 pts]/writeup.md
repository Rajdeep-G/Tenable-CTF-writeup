Refer to the writeup of spring_mvc_1

In MainController.java we have the function:-

```java
@PostMapping("/main")
        public String postMain(@RequestParam(name="magicWord", required=false, defaultValue="") String magicWord, Model model) {
		if (magicWord.equals("please"))
			model.addAttribute("flag", flags.getFlag("spring_mvc_3"));	// post main param 
		else
                	model.addAttribute("flag", flags.getFlag("spring_mvc_2"));	// post main
                return "flag";
        }
```

We can see that we need to make a post request to /main containing the following queries:-
 - name=magicWord
 - parameter magicWord either empty or not equal to 'please'

On making the post request, we will get our flag:-

## flag{flag2_de3981}