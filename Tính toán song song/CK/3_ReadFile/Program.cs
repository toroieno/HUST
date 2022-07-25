using System;
using System.IO; //read file
using System.Text;
using Alchemi.Core.Owner;

namespace SquareNumber
{
    class SquareNumber : GApplication
    {
        public static GApplication App = new GApplication();
        private static int NumPerThread;//So luong so trong 1 thread
        private static DateTime start;
        private static string wdoc; //file ghi

        [STAThread]
        static void Main(string[] args)
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;
            Console.WriteLine("BÀI TẬP RIÊNG - ĐỌC FILE");
            Console.WriteLine("Đọc file \"input.txt\"");
            string rdoc = File.ReadAllText("../../input.txt"); // file đọc
            Console.WriteLine("Chuỗi cần chuyển đổi: " + rdoc);

            Console.Write("Đưa vào số luồng cho 1 thread: ");
            NumPerThread = Int32.Parse(Console.ReadLine());

            Console.WriteLine();
            byte[] asciiBytes = Encoding.ASCII.GetBytes(rdoc); // convert ascii -> num
            int n = asciiBytes.Length;
            int NumRemain = n;
            int NumCur = 0;
            int NumberOfThread, Begin, End;
            while (NumRemain > 0)
            {
                if (NumRemain > NumPerThread)
                {
                    NumberOfThread = NumPerThread;
                }
                else
                {
                    NumberOfThread = NumRemain;
                }
                Begin = NumCur;
                NumCur += NumberOfThread;
                if (NumCur >= n) { End = n - 1; }
                else { End = NumCur - 1; }

                App.Threads.Add(new FileChange(Begin, End, asciiBytes));
                NumRemain -= NumberOfThread;
            }
            App.Connection = new GConnection("localhost", 9000, "user", "user");
            App.Manifest.Add(new ModuleDependency(typeof(FileChange).Module));
            App.ThreadFinish += new GThreadFinish(App_ThreadFinish);
            App.ApplicationFinish += new GApplicationFinish(App_ApplicationFinish);
            start = DateTime.Now;
            Console.WriteLine("Thread started!");
            App.Start();
            Console.ReadLine();

        }

        private static void App_ThreadFinish(GThread thread)
        {
            FileChange fc = (FileChange)thread;
            Console.Write("Chuyển kí tự {0}-{1} hoàn thành: ", fc.Begin, fc.End);
            wdoc = "";
            for (int i = fc.Begin; i <= fc.End; i++)
            {
                Console.Write(fc.Texts[i] + " ");
                wdoc += fc.Texts[i];
            }
            File.AppendAllText("../../output.txt", wdoc);
            Console.WriteLine();
        }
        private static void App_ApplicationFinish()
        {
            Console.WriteLine("Hoàn thành sau {0} seconds.", DateTime.Now - start);
            Console.WriteLine("Kết quả được lưu vào fie \"output.txt\"");
        }
    }
    [Serializable]
    class FileChange : GThread
    {
        public int Begin, End;
        public byte[] Nums = new byte[100];
        public char[] Texts = new char[100];
        public FileChange(int begin, int end, byte[] nums)
        {
            this.Begin = begin;
            this.End = end;
            this.Nums = nums;
        }
        private byte f(byte x)
        {
            return (byte)(2 * x + 1);
        }
        public override void Start()
        {
            for (int i = Begin; i <= End; i++)
            {
                Nums[i] = f(Nums[i]);
                if (Nums[i] >= 255) { Nums[i] -= 255; }
                Texts[i] = Convert.ToChar(Nums[i]); // convert num -> ascii
            }
        }
    }
}
