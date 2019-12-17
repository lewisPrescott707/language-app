## How to run app

### Step 1:
- Open CMD (Bash / Terminal)  
- Type `./setup.sh` and press Enter 
### Step 2:
- Type `pip install -r requirements.txt` and press Enter 
### Step 3:
- Type `python app.py` and press Enter
### Step 4:
- Open any browser (Chrome)
- Navigate to http://127.0.0.1:5000/
#### Pages
1. Verbs: http://127.0.0.1:5000/verbs
2. Adjectives: http://127.0.0.1:5000/adjectives

## Where to start
1. Read documentation below on HTML & Database
2. Render HTML with Verb 'Aller' e.g. within a table
``` html
<!doctype html>
<html>
   <body>
      <table border = 1>
         {% for key, value in result.iteritems() %}
            <tr>
               <th> {{ key }} </th>
               <td> {{ value }} </td>
            </tr>
         {% endfor %}
      </table>
   </body>
</html>
```
3. Add form to Verb page:
    - Input field
    - Submit button
    - Insert new verb in to database
    - New Verb should be shown in table (as part of step 2)
4. Add `CSS` to HTML page (Make it look pretty)
5. Follow the same with Adjectives
6. Refactor code to have reusable functions across Adjectives and Verbs

## Helpful documentation:
Interacting with the [Database](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/)   
Creating [Html](https://www.tutorialspoint.com/flask/flask_templates.htm) pages in python  
Running the website with [Flask](https://pythonspot.com/flask-web-app-with-python/)

## Glossary:
Refactor: Code refactoring is the process of restructuring existing code