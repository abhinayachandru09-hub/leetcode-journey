#LeetCode valid parentheses in c 

bool isValid(char* s) {
    char stack[10000];
    int top = -1;

    for(int i = 0; s[i] != '\0'; i++)
    {
        char ch = s[i];

        // Opening brackets
        if(ch == '(' || ch == '[' || ch == '{')
        {
            stack[++top] = ch;
        }

        // Closing brackets
        else
        {
            // Empty stack
            if(top == -1)
                return false;

            char open = stack[top--];

            if(ch == ')' && open != '(')
                return false;

            if(ch == ']' && open != '[')
                return false;

            if(ch == '}' && open != '{')
                return false;
        }
    }

    // If stack is empty, all brackets matched
    return top == -1;

}