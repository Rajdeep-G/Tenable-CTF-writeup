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

We can clearly see from the above function that we need to make a post request to /main containing the following queries:-
 - name=magicWord
 - magicWord=please

## Hurray you got the flag!!

## flag{flag3_0d431e}