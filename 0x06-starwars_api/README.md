# Making a Node.js Script Executable

If you have a Node.js script and you want to make it executable without using the `node` command, you can follow these steps.

## Step 1: Add Shebang Line

At the beginning of your Node.js script, add a shebang line that specifies the interpreter to be used. In this case, we're using Node.js. The shebang line should look like this:

```javascript
#!/usr/bin/env node
```

## Step 2: Make the Script Executable

After adding the shebang line, you need to make the script file executable. You can do this using the `chmod` command. Open your terminal and navigate to the directory where your script is located. Then, run the following command:

```bash
chmod +x your-script.js
```

Replace `your-script.js` with the actual name of your script file.

## Step 3: Run the Script

Once the script is made executable, you can run it using the `./` notation just like you would with shell scripts. Open your terminal and navigate to the directory containing your script. Then, run the script using:

```bash
./your-script.js
```

Replace `your-script.js` with the actual name of your script file.

That's it! You've now made your Node.js script executable and can run it directly using the `./` notation.

Replace `your-script.js` with the actual name of your script file. You can save this content in a Markdown file (e.g., `making-nodejs-script-executable.md`) and render it using a Markdown viewer or editor to read the instructions and steps.