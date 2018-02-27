using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            for (int i = 0; i < 1500; i++)
            {
                checkflag(i);
            }
        }
        public static string CreateMD5(string input)
        {
            using (MD5 md5 = MD5.Create())
            {
                byte[] bytes = Encoding.ASCII.GetBytes(input);
                byte[] hash = md5.ComputeHash(bytes);
                StringBuilder stringBuilder = new StringBuilder();
                for (int index = 0; index < hash.Length; ++index)
                    stringBuilder.Append(hash[index].ToString("X2"));
                return stringBuilder.ToString();
            }
        }

        private static void checkflag(int key)
        {
            StringBuilder stringBuilder = new StringBuilder();
            string str1 = "xiomara{";
            string str2 = "þæþÖîûìèýÖðæüÖíàíÖàýÖ\x00B3 ";
            string str3 = "}";
            string str4 = "DB2C17E69713C8604A91AA7A51CBA041";
            for (int index = 0; index < str2.Length; ++index)
                stringBuilder.Append((char)((uint)str2[index] ^ (uint)key));
            string input = stringBuilder.ToString();
            string md5 = CreateMD5(input);
            if (md5.Equals(str4))
            {
                Console.WriteLine("Flag is:");
                Console.WriteLine(str1 + input + str3);
            }
        }

    }
}
