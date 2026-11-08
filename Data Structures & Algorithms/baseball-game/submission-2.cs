public class Solution
{
    public int CalPoints(string[] operations)
    {
        var s = new List<int>();

        foreach (string op in operations)
        {
            if (op == "+")
            {
                // Sum the last two scores
                s.Add(s[^1] + s[^2]);
            }
            else if (op == "D")
            {
                // Double the last score
                s.Add(s[^1] * 2);
            }
            else if (op == "C")
            {
                // Remove the last score
                s.RemoveAt(s.Count - 1);
            }
            else
            {
                // Convert string to integer and add
                s.Add(int.Parse(op));
            }
        }

        // Sum up all elements
        return s.Sum();
    }
}