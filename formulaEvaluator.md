using System;
using System.Text.RegularExpressions;
using System.Linq;
using System.Collections;
using System.Data;

namespace FormulaEvaluator
{
    /// <summary>
    /// this class takes in an expression in the form of a string and evaluates it
    /// throws error if expression not in correct infix notation
    /// Author: Steven Blanco 
    /// CS 3500
    /// University of Utah
    /// </summary>
    public static class Evaluator
    {
        public delegate int Lookup(String v);
        private delegate bool Condition(Char v);


        public static int Evaluate(String exp, Lookup variableEvaluator)
        {
            Stack opStack = new Stack();
            Stack valStack = new Stack();

            string[] substrings = Regex.Split(exp, "(\\()|(\\))|(-)|(\\+)|(\\*)|(/)");

            foreach (string token in substrings)
            {
                string t = String.Concat(token.Where(c => !Char.IsWhiteSpace(c))); // trims white space, leaving only the token

                if (t.Equals("")) continue;

                else if (t.Equals("*") || t.Equals("/") || t.Equals("("))
                    opStack.Push(t);

                else if (IsCondition(t, Char.IsDigit)) // if token == Integer
                {
                    valStack.Push(t);
                    if (IsOnTop("*", opStack) || IsOnTop("/", opStack))
                        PopOperatorApplyToTopTwoStackValues(valStack, opStack);
                }

                else if (t.Equals("+") || t.Equals("-"))
                {
                    if (IsOnTop("+", opStack) || IsOnTop("-", opStack))
                        PopOperatorApplyToTopTwoStackValues(valStack, opStack);
                    opStack.Push(t);
                }

                // these two if statments and the block between check if the token is a variable
                else if (IsCondition(t, Char.IsLetterOrDigit))
                {
                    // this block of code + the if statement ensures that the variable is correctly formatted
                    // ex a4 -> a  4
                    // ex a4a4 -> a   4
                    // latter is used to check if it still matches the string
                    // the purpose of this code is to check for correctly formatted variables
                    Regex r = new Regex(@"([a-zA-Z]+)(\d+)");
                    Match list = r.Match(t);
                    string letterHalf = list.Groups[1].Value;
                    string numberHalf = list.Groups[2].Value;

                    if (t.Equals(list.ToString()))
                    {
                        try
                        {
                            String num = Convert.ToString(variableEvaluator(t));
                            valStack.Push(num);
                            if (IsOnTop("*", opStack) || IsOnTop("/", opStack))
                                PopOperatorApplyToTopTwoStackValues(valStack, opStack);
                        }
                        catch
                        {
                            throw new ArgumentException("variable has no value");
                        }
                    }
                    else
                        throw new ArgumentException("Invalid Variable Format");
                }

                else if (t.Equals(")"))
                {
                    if (IsOnTop("+", opStack) || IsOnTop("-", opStack))
                    {
                        PopOperatorApplyToTopTwoStackValues(valStack, opStack);
                        if (IsOnTop("(", opStack)) opStack.Pop();

                        else throw new ArgumentException("Expression formatted incorrectly");

                        if (IsOnTop("*", opStack) || IsOnTop("/", opStack))
                        {
                            PopOperatorApplyToTopTwoStackValues(valStack, opStack);
                        }
                    }
                    else if (IsOnTop("(", opStack))
                    {
                        opStack.Pop();
                    }
                    else
                    {
                        throw new ArgumentException("Expression formatted incorrectly");
                    }
                }
            }
            if (opStack.Count == 0 && valStack.Count == 1)
                return Convert.ToInt32(valStack.Pop());
            else if (((IsOnTop("+", opStack) || IsOnTop("-", opStack)) && opStack.Count == 1) && valStack.Count == 2)
            {
                PopOperatorApplyToTopTwoStackValues(valStack, opStack);
                return Convert.ToInt32(valStack.Pop());
            }
            else if (((IsOnTop("*", opStack) || IsOnTop("/", opStack)) && opStack.Count == 1) && valStack.Count == 2)
            {
                PopOperatorApplyToTopTwoStackValues(valStack, opStack);
                return Convert.ToInt32(valStack.Pop());
            }
            else
            {
                throw new ArgumentException("Expression formatted incorrectly");
            }
        }

        /// <summary>
        /// test all characters in a string if they meet a certain value
        /// ex: if they are all character, if they are all numbers etc
        /// </summary>
        /// <param name="x"></param>
        /// <param name="func"></param>
        /// <returns>bool</returns>
        private static bool IsCondition(String x, Condition func)
        {
            char[] characters = x.ToCharArray();
            foreach (char character in characters)
            {
                if (!func(character))
                    return false;
            }
            return true;
        }

        /// <summary>
        /// performs operation on 2 numbers and a value then returns it
        /// num2 <op> num1 = result
        /// </summary>
        /// <param name="val1"></param>
        /// <param name="val2"></param>
        /// <param name="op"></param>
        /// <returns></returns>
        private static int PerformOperation(string val2, string op, string val1)
        {
            int num1 = Convert.ToInt32(val1);
            int num2 = Convert.ToInt32(val2);
            if (op.Equals("/"))
                return num2 / num1;

            else if (op.Equals("*"))
                return num2 * num1;

            else if (op.Equals("-"))
                return num2 - num1;

            // op.Equals("+")
            return num2 + num1;
        }

        /// <summary>
        /// pops the operator and the value stack twice, then applies the operator on the two values
        /// </summary>
        private static void PopOperatorApplyToTopTwoStackValues(Stack valStack, Stack opStack)
        {

            try
            {
                string num1 = valStack.Pop().ToString();
                string num2 = valStack.Pop().ToString();
                string op = opStack.Pop().ToString();

                int output = PerformOperation(num2, op, num1);
                valStack.Push(output);
            }
            catch (DivideByZeroException)
            {
                throw new ArgumentException("Cannot divide by 0");
            }
            catch (InvalidOperationException)
            {
                throw new ArgumentException("Expression formatted incorrectly");
            }
        }

        /// <summary>
        /// gets rid of redundent code
        /// basically <stackObj>.Peek() but doesn't crash if stack is empty
        /// </summary>
        /// <param name="x"></param>
        /// <param name="stack"></param>
        /// <returns></returns>
        private static bool IsOnTop(string x, Stack stack)
        {
            return stack.Count > 0 && stack.Peek().Equals(x);
        }
    }
}
