using System;
using Alchemi.Core.Owner;

namespace Integral
{
    class Intergral : GApplication
    {
        public static GApplication App = new GApplication();
        private static int NumPerThread;//So luong so trong 1 thread
        private static DateTime start;
        private static double h;
        private static double I; //file ghi
        static double f(double x)
        {
            return (double)(Math.Sin(Math.PI+Math.Pow(x,2))+(Math.Pow(x,2)+1)/2+Math.PI);
        }
        [STAThread]
        static void Main(string[] args)
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;
            Console.WriteLine("BÀI TẬP CHUNG - TÍNH TÍCH PHÂN");

            Console.Write("Nhập: n = ");
            int n = Convert.ToInt32(Console.ReadLine());
            double a = 0; // cận dưới
            double b = n; // cận trên
            I = (f(a) + f(b)) / 2;
            Console.Write("Số khoảng: ");
            int kc = Int32.Parse(Console.ReadLine());
            h = (b - a) / kc;
            Console.Write("Đưa vào số luồng cho 1 thread: ");
            NumPerThread = Int32.Parse(Console.ReadLine());

            Console.WriteLine();
            int NumRemain = kc;
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
                if (NumCur >= kc) { End = kc; }
                else { End = NumCur - 1; }

                App.Threads.Add(new CalcIntegral(Begin, End, h));
                NumRemain -= NumberOfThread;
            }
            App.Connection = new GConnection("localhost", 9000, "user", "user");
            App.Manifest.Add(new ModuleDependency(typeof(CalcIntegral).Module));
            App.ThreadFinish += new GThreadFinish(App_ThreadFinish);
            App.ApplicationFinish += new GApplicationFinish(App_ApplicationFinish);
            start = DateTime.Now;
            Console.WriteLine("Thread started!");
            App.Start();
            Console.ReadLine();
        }
        private static void App_ThreadFinish(GThread thread)
        {
            CalcIntegral ci = (CalcIntegral)thread;
            Console.WriteLine("Tính đoạn {0}-{1} hoàn thành", ci.x[ci.Begin], ci.x[ci.End]);
            for (int i = ci.Begin; i <= ci.End; i++)
            {
                I += ci.Nums[i];
            }
        }
        private static void App_ApplicationFinish()
        {

            Console.WriteLine("Kết quả tính tích phân: {0}", I*h);
            Console.WriteLine("Hoàn thành sau {0} seconds.", DateTime.Now - start);
        }
    }
    [Serializable]
    class CalcIntegral : GThread
    {
        public int Begin, End;
        public double[] Nums = new double[100];
        public double[] x = new double[100];
        private double h;
        public CalcIntegral(int begin, int end, double kc)
        {
            this.Begin = begin;
            this.End = end;
            this.h = kc;
        }
        private double f(double x)
        {
            return (double)(Math.Sin(Math.PI + Math.Pow(x, 2)) + (Math.Pow(x, 2) + 1) / 2 + Math.PI);
        }
        public override void Start()
        {
            for (int i = Begin; i <= End; i++)
            {
                x[i] = i * h;
                Nums[i] = f(x[i]);
            }
        }
    }
}
