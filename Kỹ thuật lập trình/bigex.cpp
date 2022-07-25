#include<iostream>
#include<stdlib.h>
#include<fstream> // xu li file
#include<math.h>
#include<iomanip>
#include<time.h> // tao thoi gian - random
#include<conio.h>
#include<cstdlib>
#include<windows.h> //tao mau va toa do
using namespace std;

//menu
void gotoxy(int x, int y); // toa do
void menupop();
//sinh ma tran ngau nhien
void RandomMatrix(int choice);
void XuatMaTran(float a[][100], int row, int col);
//cac phep toan tren 2 ma tran
void CongHaiMaTran();
void TruHaiMaTran();
void NhanHaiMaTran();
void NhanVoHuong();
//tinh nghich dao
void PhanPhuDaiSo(float a[][100], int n);
void GaussJordan(float a[][100], int n);
void TimNghichDao();
// tim hang
void TimHang(float a[][100], int r, int c);
void TimHangMaTran();
//tinh dinh thuc
double Det(float a[][100], int n);
void TinhDinhThuc();
//tim tri rieng
void CreateMatrixM(float a[][100], float b[][100], int n, int row);
void CreateMatrixM_1(float a[][100], float b[][100], int n, int row);
void TichMaTran(float a[][100], float b[][100], float c[][100], int n);
//giai phuong trinh bac n
float f(float x, float a[100], int n);
float fx(float x, float a[100], int n);
float GiaiNghiem(float x, float a[100], int n, int &chot);
void ChiaDaThuc(float x, float a[100], int &n);
void GiaiPhuongTrinh(float b[][100], int n);
void TimTriRieng();
//tim vecto rieng
void TriRieng(float b[][100], int n, float E[][100]);
void VectoRieng(float x, int n1, float E[][100]);
void TimVectoRieng();

int main()
{
	menupop();
	return 0;	
}

//tao menu lam viec
//ham toa do
void gotoxy(int x, int y)
{
    static HANDLE h = NULL;  
    if(!h)
        h = GetStdHandle(STD_OUTPUT_HANDLE);
    COORD c = { x, y };  
    SetConsoleCursorPosition(h,c);
}
//menu pop
//control - phim MUI TEN LEN, XUONG va phim ENTER
void menupop(){
	char key, k;
	int choice;
	//khoi tao mau
	HANDLE hConsoleColor;
	hConsoleColor = GetStdHandle(STD_OUTPUT_HANDLE);
	choice = 1;
		
	// create khung menu
	SetConsoleTextAttribute(hConsoleColor, 5);
	gotoxy(1,0); cout << "MENU" ;
	gotoxy(1,1); cout << "nhan ESC de thoat chuong trinh!" ;
	gotoxy(2,3); cout << "-------------------------------------------------------------------------------" << endl;
	gotoxy(2,4); cout << "|" ; gotoxy(80,4); cout << "|";
	gotoxy(2,5); cout << "|" ; gotoxy(80,5); cout << "|";
	gotoxy(2,6); cout << "|" ; gotoxy(80,6); cout << "|";
	gotoxy(2,7); cout << "|" ; gotoxy(80,7); cout << "|";
	gotoxy(2,8); cout << "|" ; gotoxy(80,8); cout << "|";
	gotoxy(2,9); cout << "|" ; gotoxy(80,9); cout << "|";
	gotoxy(2,10); cout << "|" ; gotoxy(80,10); cout << "|";
	gotoxy(2,11); cout << "|" ; gotoxy(80,11); cout << "|";
	gotoxy(2,12); cout << "|" ; gotoxy(80,12); cout << "|";
	gotoxy(2,13); cout << "|" ; gotoxy(80,13); cout << "|";
	gotoxy(2,14); cout << "-------------------------------------------------------------------------------" << endl;
	gotoxy(2,15); cout << "|" ; cout << "Chuc nang: "; gotoxy(80,15); cout << "|";
	gotoxy(2,16); cout << "|" ; cout << "File: "; gotoxy(80,16); cout << "|";
	gotoxy(2,17); cout << "|" ; gotoxy(80,17); cout << "|";
	gotoxy(2,18); cout << "|" ; gotoxy(80,18); cout << "|";
	gotoxy(2,19); cout << "|" ; gotoxy(80,19); cout << "|";
	gotoxy(2,20); cout << "-------------------------------------------------------------------------------" << endl;
	gotoxy(2,21); cout << "|" ; cout << "Ket qua: "; gotoxy(80,21); cout << "|";
	gotoxy(2,22); cout << "|" ; gotoxy(80,22); cout << "|";
	gotoxy(2,23); cout << "|" ; gotoxy(80,23); cout << "|";
	gotoxy(2,24); cout << "|" ; gotoxy(80,24); cout << "|";
	gotoxy(2,25); cout << "|" ; gotoxy(80,25); cout << "|";
	gotoxy(2,26); cout << "-------------------------------------------------------------------------------" << endl;
	
	while(true){
		//system("cls");
		//set color - control
		SetConsoleTextAttribute(hConsoleColor, 9);
		if (choice == 1)
			SetConsoleTextAttribute(hConsoleColor, 15);
		gotoxy(4,4); cout << "Sinh ma tran ngau nhien" << endl;
			
		SetConsoleTextAttribute(hConsoleColor, 9);
		if (choice == 2)
			SetConsoleTextAttribute(hConsoleColor, 15);
		gotoxy(4,5); cout << "Cong hai ma tran" << endl;
			
		SetConsoleTextAttribute(hConsoleColor, 9);
		if (choice == 3)
			SetConsoleTextAttribute(hConsoleColor, 15);
		gotoxy(4,6); cout << "Tru hai ma tran" << endl;
			
		SetConsoleTextAttribute(hConsoleColor, 9);
		if (choice == 4)
			SetConsoleTextAttribute(hConsoleColor, 15);
		gotoxy(4,7); cout << "Nhan hai ma tran" << endl;
		
		SetConsoleTextAttribute(hConsoleColor, 9);
		if (choice == 5)
			SetConsoleTextAttribute(hConsoleColor, 15);
		gotoxy(4,8); cout << "Nhan vo huong ma tran voi mot so thuc" << endl;
		
		SetConsoleTextAttribute(hConsoleColor, 9);
		if (choice == 6)
			SetConsoleTextAttribute(hConsoleColor, 15);
		gotoxy(4,9); cout << "Tim ma tran nghich dao cua ma tran vuong" << endl;
		
		SetConsoleTextAttribute(hConsoleColor, 9);
		if (choice == 7)
			SetConsoleTextAttribute(hConsoleColor, 15);
		gotoxy(4,10); cout << "Tinh hang cua ma tran" << endl;
		
		SetConsoleTextAttribute(hConsoleColor, 9);
		if (choice == 8)
			SetConsoleTextAttribute(hConsoleColor, 15);
		gotoxy(4,11); cout << "Tinh dinh thuc cua ma tran" << endl;
		
		SetConsoleTextAttribute(hConsoleColor, 9);
		if (choice == 9)
			SetConsoleTextAttribute(hConsoleColor, 15);
		gotoxy(4,12); cout << "Tim tri rieng" << endl;
		
		SetConsoleTextAttribute(hConsoleColor, 9);
		if (choice == 10)
			SetConsoleTextAttribute(hConsoleColor, 15);
		gotoxy(4,13); cout << "Tim vecto rieng" << endl;
		//bat su kien tu ban phim
		key = getch();
		if (key == 72) // mui ten len
			if (choice == 1)
				choice = 10;
			else
				choice--;
		if (key == 80) // mui ten xuong
			if (choice == 10)
				choice = 1;
			else
				choice++;
		if (key == 13){ // phim enter
			SetConsoleTextAttribute(hConsoleColor, 2);
			switch(choice){
				case 1: 
					gotoxy(14,15); 
					cout << "SINH MA TRAN NGAU NHIEN                 " << endl;
					RandomMatrix(choice);
					getch();
					break;
				case 2: 
					gotoxy(14,15);
					cout << "CONG HAI MA TRAN                        " << endl;
					CongHaiMaTran();
					getch(); 
					break;
				case 3: 
					gotoxy(14,15); 
					cout << "TRU HAI MA TRAN                         " << endl; 
					TruHaiMaTran();
					getch(); 
					break;
				case 4: 
					gotoxy(14,15); 
					cout << "NHAN HAI MA TRAN                        " << endl;
					NhanHaiMaTran();
					getch(); 
					break;
				case 5: 
					gotoxy(14,15); 
					cout << "NHAN VO HUONG MA TRAN VOI MOT SO THUC   " << endl; 
					NhanVoHuong();
					getch(); 
					break;
				case 6: 
					gotoxy(14,15); 
					cout << "TIM MA TRAN NGHICH DAO CUA MA TRAN VUONG" << endl; 
					TimNghichDao();
					getch(); 
					break;
				case 7: 
					gotoxy(14,15); 
					cout << "TINH HANG CUA MA TRAN                   " << endl; 
					TimHangMaTran();
					getch(); 
					break;
				case 8: 
					gotoxy(14,15); 
					cout << "TINH DINH THUC CUA MA TRAN              " << endl;
					TinhDinhThuc();
					getch(); 
					break;
				case 9: 
					gotoxy(14,15); 
					cout << "TIM TRI RIENG                           " << endl; 
					TimTriRieng();
					getch(); 
					break;
				case 10: 
					gotoxy(14,15); 
					cout << "TIM VECTO RIENG                        " << endl; 
					TimVectoRieng();
					getch(); 
					break;
			}
		}
		SetConsoleTextAttribute(hConsoleColor, 7);
		if (key == 27){ // phim esc
			break;
		}
		gotoxy(14,15); cout << "                                                " << endl;
		gotoxy(8,16); cout << "                                                "; 
		gotoxy(4,17); cout << "                                                ";
		gotoxy(4,18); cout << "                                                ";
		gotoxy(4,19); cout << "                                                ";
		gotoxy(4,22); cout << "                                                ";
		gotoxy(4,23); cout << "                                                ";
	}
	system("cls");
	gotoxy(30,10);
	SetConsoleTextAttribute(hConsoleColor, 11);
	cout << "Thanks and see u again!";
	getch();
}
// sinh ma tran voi kich thuoc ngau nhien
void RandomMatrix(int choice){
	fstream file;
	char key;
	int row, col, ran, flag = 0;
	int a[100][100];
	
	//khoi tao mau - color
	HANDLE hConsoleColor;
	hConsoleColor = GetStdHandle(STD_OUTPUT_HANDLE);
	
	//while - chon sinh vao file 1 hay 2
	while(1){
		SetConsoleTextAttribute(hConsoleColor, 1);
		if (choice == 1)
			SetConsoleTextAttribute(hConsoleColor, 7);
		gotoxy(4,17); cout << "Sinh ma tran ngau nhien vao file \"matrix1.txt\" " << endl;
		
		SetConsoleTextAttribute(hConsoleColor, 1);
		if (choice == 2)
			SetConsoleTextAttribute(hConsoleColor, 7);
		gotoxy(4,18); cout << "Sinh ma tran ngau nhien vao file \"matrix2.txt\"" << endl;
		//bat su kien tu ban phim
		key = getch();
		if (key == 72) // mui ten len
			if (choice == 1)
				choice = 2;
			else
				choice--;
		if (key == 80) // mui ten xuong
			if (choice == 2)
				choice = 1;
			else
				choice++;
		SetConsoleTextAttribute(hConsoleColor, 1);
		if (key == 13){ // phim enter
			break;
		}
	}
	if (choice == 1){
		file.open("matrix1.txt", ios::out);
		if (file.fail()){
			gotoxy(4,22); cout << "Fail to open file \"matrix1.txt\" ";
			file << "Fail" << endl;
			flag = 1;
		}
		SetConsoleTextAttribute(hConsoleColor, 6);
		gotoxy(9,16); cout << "matrix1.txt";
	}
	else{
		file.open("matrix2.txt", ios::out);
		if (file.fail()){
			gotoxy(4,22); cout << "Fail to open file \"matrix2.txt\" ";
			file << "Fail" << endl;
			flag = 1;
		}
		SetConsoleTextAttribute(hConsoleColor, 6);
		gotoxy(9,16); cout << "matrix2.txt";
	}
	//sau khi mo 2 file thanh cong
	if (flag == 0){
		srand((int) time(0)); //de cac lan sinh khac nhau
		row = rand() % 100+1; //sinh hang ngau nhien
		col = rand() % 100+1; //sinh cot ngau nhien
		file << row << " " << col << endl;
		for (int i = 0; i < row; i++){
			for (int j = 0; j < col; j++){
				ran = rand(); //sinh cac phan tu ngau nhien
				file << ran << " ";
			}
			file << endl;
		}
		//hien thi ra man hinh - thong bao thanh cong
		SetConsoleTextAttribute(hConsoleColor, 4);
		gotoxy(4,22);  cout << "Complete!";
		gotoxy(4,23); cout << "Sinh ma tran thanh cong" << endl;
	}
	
	file.close();
}
//ham xuat ma tran bat ki
void XuatMaTran(float a[][100], int row, int col){
	fstream fileKQ;
	
	fileKQ.open("ketqua.txt", ios::app);
	//fileKQ << "ma tran: " << row << "\t" << col << endl;
	
	for (int i = 0; i < row; i++){
		for (int j = 0; j < col; j++)
			fileKQ << a[i][j] << " ";
		fileKQ << endl;
	}
	
	fileKQ.close();
}
//ham cong hai ma tran
void CongHaiMaTran(){
	fstream file1, file2, fileKQ;
	float a[100][100], b[100][100];
	int m, n, r1, c1, r2, c2, i, j, flag = 0;
	
	//khoi tao mau - color
	HANDLE hConsoleColor;
	hConsoleColor = GetStdHandle(STD_OUTPUT_HANDLE);
	
	SetConsoleTextAttribute(hConsoleColor, 6);
	gotoxy(8,16); cout << "\"matrix1.txt\" and \"matrix2.txt\"";
	//mo file
	file1.open("matrix1.txt", ios::in);
	if (file1.fail()){
		gotoxy(4,22); cout << "Fail to open file \"matrix1.txt\" ";
		flag = 1;
	}
	file2.open("matrix2.txt", ios::in);
	if (file2.fail()){
		gotoxy(4,22); cout << "Fail to open file \"matrix2.txt\" ";
		flag = 1;
	}
	fileKQ.open("ketqua.txt", ios::app);
	if (fileKQ.fail()){
		gotoxy(4,22); cout << "Fail to open file \"ketqua.txt\" ";
		flag = 1;
	}
	//mo file thanh cong
	if (flag == 0){
		fileKQ << "---------------------------------------------------------------" << endl;
		fileKQ << "Thuc hien cong hai ma tran: " << endl;
		//doc cot va hang cua 2 ma tran
		file1 >> r1 >> c1; //ma tran 1
		file2 >> r2 >> c2; //ma tran 2
		//kiem tra 2 ma tran co cung kich thuoc khong
		if ((r1 != r2) or (c1 != c2)){
			SetConsoleTextAttribute(hConsoleColor, 4);
			gotoxy(4,22); cout << "Khong the thuc hien cong hai ma tran!" << endl;
			fileKQ << "Fail" << endl;
		}
		else{
			//lay ma tran tu file thu nhat
			fileKQ << "ma tran 1: " << endl;
			i = 0;
			j = 0;
			while (!file1.eof()){
				file1 >> a[i][j];
				if (j < c1-1)
					j++;
				else{
					j = 0;
					i++;
				}
			}
			XuatMaTran(a, r1, c1);
			fileKQ << endl;
			//lay ma tran tu file thu hai
			fileKQ << "ma tran 2: " << endl;
			i = 0;
			j = 0;
			while (!file2.eof()){
				file2 >> b[i][j];
				if (j < c2-1)
					j++;
				else{
					j = 0;
					i++;
				}
			}
			XuatMaTran(b, r2, c2);
			fileKQ << endl;
			//dua ket qua vao fileKQ
			fileKQ << "Ket qua: " << endl;
			for (i = 0; i < r1; i++){
				for (j = 0; j < c1; j++)
					fileKQ << a[i][j]+b[i][j] << " ";
				fileKQ << endl;
			}		
			//hien thi ra man hinh - thong bao thanh cong
			SetConsoleTextAttribute(hConsoleColor, 4);
			gotoxy(4,22);  cout << "Complete!";
			gotoxy(4,23); cout << "Ket qua duoc luu vao file \"ketqua.txt\" ";
		}
	}
	
	file1.close();
	file2.close();
	fileKQ.close();
}
void TruHaiMaTran(){
	fstream file1, file2, fileKQ;
	float a[100][100], b[100][100];
	int m, n, r1, c1, r2, c2, i = 0,j = 0, flag = 0;
	
	//khoi tao mau - color
	HANDLE hConsoleColor;
	hConsoleColor = GetStdHandle(STD_OUTPUT_HANDLE);
	
	SetConsoleTextAttribute(hConsoleColor, 6);
	gotoxy(8,16); cout << "\"matrix1.txt\" and \"matrix2.txt\"";
	file1.open("matrix1.txt", ios::in);
	if (file1.fail()){
		gotoxy(4,22); cout << "Fail to open file \"matrix1.txt\" ";
		flag = 1;
	}
	file2.open("matrix2.txt", ios::in);
	if (file2.fail()){
		gotoxy(4,22); cout << "Fail to open file \"matrix2.txt\" ";
		flag = 1;
	}
	fileKQ.open("ketqua.txt", ios::app);
	if (fileKQ.fail()){
		gotoxy(4,22); cout << "Fail to open file \"ketqua.txt\" ";
		flag = 1;
	}
	if (flag == 0){
		fileKQ << "---------------------------------------------------------------" << endl;
		fileKQ << "Thuc hien tru hai ma tran: " << endl;
		file1 >> r1 >> c1;
		file2 >> r2 >> c2;
		//kiem tra 2 ma tran co cung kich thuoc khong
		if ((r1 != r2) or (c1 != c2)){
			SetConsoleTextAttribute(hConsoleColor, 4);
			gotoxy(4,22); cout << "Khong the thuc hien tru hai ma tran!" << endl;
			fileKQ << "Fail" << endl;
		}
		else{
			//lay ma tran tu file thu nhat
			fileKQ << "ma tran 1: " << endl;
			i = 0;
			j = 0;
			while (!file1.eof()){
				file1 >> a[i][j];
				if (j < c1-1)
					j++;
				else{
					j = 0;
					i++;
				}
			}
			XuatMaTran(a, r1, c1);
			fileKQ << endl;
			//lay ma tran tu file thu hai
			fileKQ << "ma tran 2: " << endl;
			i = 0;
			j = 0;
			while (!file2.eof()){
				file2 >> b[i][j];
				if (j < c2-1)
					j++;
				else{
					j = 0;
					i++;
				}
			}
			XuatMaTran(b, r2, c2);
			fileKQ << endl;
			//xuat ket qua ra fileKQ
			fileKQ << "Ket qua: " << endl;
			for (i = 0; i < r1; i++){
				for (j = 0; j < c1; j++)
					fileKQ << a[i][j]-b[i][j] << " ";
				fileKQ << endl;
			}		
			//hien thi ra man hinh - thong bao thanh cong
			SetConsoleTextAttribute(hConsoleColor, 4);
			gotoxy(4,22);  cout << "Complete!";
			gotoxy(4,23); cout << "Ket qua duoc luu vao file \"ketqua.txt\" ";
		}
	}
	
	file1.close();
	file2.close();
	fileKQ.close();
}
void NhanHaiMaTran(){
	fstream file1, file2, fileKQ;
	float a[100][100], b[100][100];
	int r1, c1, r2, c2, i ,j, k, tmp, flag = 0;
	
	//khoi tao mau - color
	HANDLE hConsoleColor;
	hConsoleColor = GetStdHandle(STD_OUTPUT_HANDLE);
	
	SetConsoleTextAttribute(hConsoleColor, 6);
	gotoxy(8,16); cout << "\"matrix1.txt\" and \"matrix2.txt\"";
	//mo file
	file1.open("matrix1.txt", ios::in);
	if (file1.fail()){
		gotoxy(4,22); cout << "Fail to open file \"matrix1.txt\" ";
		flag = 1;
	}
	file2.open("matrix2.txt", ios::in);
	if (file2.fail()){
		gotoxy(4,22); cout << "Fail to open file \"matrix2.txt\" ";
		flag = 1;
	}
	fileKQ.open("ketqua.txt", ios::app);
	if (fileKQ.fail()){
		gotoxy(4,22); cout << "Fail to open file \"ketqua.txt\" ";
		flag = 1;
	}
	//mo file thanh cong
	if (flag == 0){ 
		fileKQ << "--------------------------" << endl;
		fileKQ << "Thuc hien nhan hai ma tran:" << endl;
		file1 >> r1 >> c1;
		file2 >> r2 >> c2;
		//kiem tra cot ma tran 1 co bang hang ma tran 2 khong
		if (c1 != r2){
			SetConsoleTextAttribute(hConsoleColor, 4);
			gotoxy(4,22); cout << "Khong the thuc hien nhan hai ma tran!" << endl;
			fileKQ << "Fail" << endl;
		}
		else{
			//lay ma tran tu file thu nhat
			fileKQ << "ma tran 1: " << endl;
			i = 0;
			j = 0;
			while (!file1.eof()){
				file1 >> a[i][j];
				if (j < c1-1)
					j++;
				else{
					j = 0;
					i++;
				}
			}
			XuatMaTran(a, r1, c1);
			fileKQ << endl;
			//lay ma tran tu file thu hai
			fileKQ << "ma tran 2: " << endl;
			i = 0;
			j = 0;
			while (!file2.eof()){
				file2 >> b[i][j];
				if (j < c2-1)
					j++;
				else{
					j = 0;
					i++;
				}
			}
			XuatMaTran(b, r2, c2);
			fileKQ << endl;
			//xuat ket qua phep nhan
			fileKQ << "Ket qua: " << endl;
			//thuc hien nhan ma tran 1 a[][] và ma tran 2 b[][]
			for (i = 0; i < r1; i++){
				for (j = 0; j < c2; j++){
					tmp = 0;
					for (k = 0; k < r2; k++){
						tmp += a[i][k]*b[k][j];
					}
					fileKQ << tmp << " ";
				}
				fileKQ << endl;
			}
			//hien thi ra man hinh - thuc hien thanh cong
			SetConsoleTextAttribute(hConsoleColor, 4);
			gotoxy(4,22);  cout << "Complete!";
			gotoxy(4,23); cout << "Ket qua duoc luu vao file \"ketqua.txt\" ";
		}
	}
	
	file1.close();
	file2.close();
	fileKQ.close();
}
//nhan vo huong ma tran voi mot so thuc
void NhanVoHuong(){
	fstream file, fileKQ;
	float a[100][100];
	int row, col, i, j, flag = 0;
	float n, tmp;
	
	//khoi tao mau - color
	HANDLE hConsoleColor;
	hConsoleColor = GetStdHandle(STD_OUTPUT_HANDLE);
	
	SetConsoleTextAttribute(hConsoleColor, 6);
	gotoxy(9,16); cout << "matrix1.txt";
	//mo file
	file.open("matrix1.txt", ios::in);
	if (file.fail()){
		gotoxy(4,22); cout << "Fail to open file \"matrix1.txt\" ";
		flag = 1;
	}
	fileKQ.open("ketqua.txt", ios::app);
	if (fileKQ.fail()){
		gotoxy(4,22); cout << "Fail to open file \"ketqua.txt\" ";
		flag = 1;
	}
	//mo file thanh cong
	if (flag == 0){
		SetConsoleTextAttribute(hConsoleColor, 1);
		gotoxy(4,17); cout << "Nhap vao so thuc bat ki: ";
		cin >> n;
		
		fileKQ << "-------------------------------------------------" << endl;
		fileKQ << "Thuc hien nhan vo huong ma tran voi mot so thuc: " << endl;
		//lay ma tran tu file
		file >> row >> col;
		fileKQ << "ma tran: " << endl;
		i = 0;
		j = 0;
		while (!file.eof()){
			file >> a[i][j];
			if (j < col-1)
				j++;
			else{
				j = 0;
				i++;
			}
		}
		XuatMaTran(a, row, col);
		fileKQ << endl;
		
		fileKQ << "Nhan vo huong voi so thuc: " << n << endl;
		//thuc hien phep nhan
		fileKQ << "\nKet qua: " << endl;
		for (i = 0; i < row; i++){
			for (j = 0; j < col; j++)
				fileKQ << a[i][j] * n << " ";
			fileKQ << endl;
		}
		//hien thi ra man hinh - thuc hien thanh cong
		SetConsoleTextAttribute(hConsoleColor, 4);
		gotoxy(4,22);  cout << "Complete!";
		gotoxy(4,23); cout << "Ket qua duoc luu vao file \"ketqua.txt\" ";
	}
	
	file.close();
	fileKQ.close();
}
// tim nghich dao - phan phu dai so - A_1=1/detA*A_T
void PhanPhuDaiSo(float a[][100], int n){
	fstream fileKQ;
	float b[100][100], c[100][100];
	int i, j, k, l, i1, j1;
	float det, tmp, detC;
	
	//khoi tao mau - color
	HANDLE hConsoleColor;
	hConsoleColor = GetStdHandle(STD_OUTPUT_HANDLE);
	
	fileKQ.open("ketqua.txt", ios::app);
	
	//chuyen vi ma tran
	fileKQ << "Lap ma tran chuyen vi A' cua A: " << endl;
	for (i = 0; i < n; i++)
		for (j = 0; j < n; j++)
			if (i < j){
				tmp = a[i][j];
				a[i][j] = a[j][i];
				a[j][i] = tmp;
			}
	XuatMaTran(a, n, n);
	//tinh ma tran phu dai so
	fileKQ << "Lap ma tran phu hop A* cua A': " << endl;
	i = 0;
	j = 0;
	while(i < n and j < n){
		i1 = 0;
		j1 = 0;
		//lay ra ma tran cap thap hon tuong ung
		for (k = 0; k < n; k++)
			for (l = 0; l < n; l++)
				if (k != i and l != j){
					c[i1][j1] = a[k][l];
					if (j1 < n-2)
						j1++;
					else{
						j1 = 0;
						i1++;
					}
				}
		detC = Det(c, n-1); //thuc hien tinh dinh thuc ma tran do
		b[i][j] = pow(-1, (i+j)) * detC; //ap dung cong thuc phu dai so
		if (j < n-1)
			j++;
		else{
			i++;
			j = 0;
		}
	}
	XuatMaTran(b, n, n);
	//Tinh ma tran nghich dao
	fileKQ << "Tinh ma tran nghich dao: A_1 = 1/det(A) * A*" << endl;
	det = 1/Det(a, n);
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
				b[i][j] *= det;
	fileKQ << "Ket qua: " << endl;
	XuatMaTran(b, n, n);
	//hien thi ra man hinh - thuc hien thanh cong
	SetConsoleTextAttribute(hConsoleColor, 4);
	gotoxy(4,22);  cout << "Complete!";
	gotoxy(4,23); cout << "Ket qua duoc luu vao file \"ketqua.txt\" ";
	
	fileKQ.close();
}
// tim nghich dao - Gauss-jordan
void GaussJordan(float a[][100], int n){
	fstream fileKQ;
	float E[100][100];
	int i, j, k, l;
	float tmp;
	
	//khoi tao mau - color
	HANDLE hConsoleColor;
	hConsoleColor = GetStdHandle(STD_OUTPUT_HANDLE);
	
	fileKQ.open("ketqua.txt", ios::app);
	// khoi tao ma tran don vi
	fileKQ << "Khoi tao ma tran don vi E: " << endl;
	for (i = 0; i < n; i++)
		for (j = 0; j < n; j++)
			if (i == j)
				E[i][j] = 1;
			else
				E[i][j] = 0;
	XuatMaTran(E, n, n);
	// khu gauss - bac thang
	
	//kiem tra phan tu dau khac 0
	i = 0;
	j = 0;
	if (a[i][j] == 0){ //neu bang 0, ta thuc hien dao cho voi phan tu khac 0
		for (k = i+1; k < n; k++)
			if (a[k][j] != 0){ 
				for (l = i; l < n; l++){
					tmp = a[i][l];
					a[i][l] = a[k][l];
					a[k][l] = tmp;
				}
				break;
			}
		}
	//thuc hien chuyen ve tam giac
	fileKQ << "Chuyen doi A|E thanh E|B: " << endl;
	fileKQ << "step 1: " << endl;
	//step1 - trigle1 - tam giac tren
	i = 0;
	j = 0;
	while (i < n and j < n){
		for (k = i+1; k < n; k++)
			if (a[k][j] != 0){
				tmp = (float)a[k][j] / (float)a[i][j];
				for (l = 0; l < n; l++){
					a[k][l] -= a[i][l] * tmp;
					E[k][l] -= E[i][l] * tmp;
				}
			}
		i++;
		j++;
	}
	fileKQ << "A: " << endl;
	XuatMaTran(a, n, n);
	fileKQ << "E: " << endl;
	XuatMaTran(E, n, n);
	//step2 - trigle2 - ma tran duong cheo
	fileKQ << "step 2: " << endl;
	i = n-1;
	j = n-1;
	while (i > 0 and j > 0){
		for (k = i-1; k >= 0; k--)
			if (a[k][j] != 0){
				tmp = (float)a[k][j] / (float)a[i][j];
				for (l = n-1; l >= 0; l--){
					a[k][l] -= a[i][l] * tmp;
					E[k][l] -= E[i][l] * tmp;
				}
			}
		i--;
		j--;
	}
	fileKQ << "A: " << endl;
	XuatMaTran(a, n, n);
	fileKQ << "E: " << endl;
	XuatMaTran(E, n, n);
	//step3 - diagonal - dua ve ma tran don vi
	fileKQ << "step 3: " << endl;
	for (i = 0; i < n; i++){
		if (a[i][i] != 1){
			tmp = 1.0 / (float)a[i][i];
			a[i][i] *= tmp;
			for (j = 0; j < n; j++)
				E[i][j] *= tmp;
		}	
	} 
	fileKQ << "A: " << endl;
	XuatMaTran(a, n, n);
	fileKQ << "E: " << endl;
	XuatMaTran(E, n, n);
	//complete
	fileKQ << "Ket qua: " << endl;
	XuatMaTran(E, n, n);
	//hien thi ra man hình - thuc hien thanh cong
	SetConsoleTextAttribute(hConsoleColor, 4);
	gotoxy(4,22);  cout << "Complete!";
	gotoxy(4,23); cout << "Ket qua duoc luu vao file \"ketqua.txt\" ";
	
	fileKQ.close();
}
// choice 1 in 2 PP
void TimNghichDao(){
	fstream file, fileKQ;
	char key;
	int row, col, choice = 1, i = 0, j = 0, flag = 0;
	float a[100][100], b[100][100];
	
	//khoi tao mau - color
	HANDLE hConsoleColor;
	hConsoleColor = GetStdHandle(STD_OUTPUT_HANDLE);
			
	SetConsoleTextAttribute(hConsoleColor, 6);
	gotoxy(8,16); cout << "matranvuong.txt";
	//mo file
	file.open("matranvuong.txt", ios::in);
	if (file.fail()){
		gotoxy(4,22); cout << "Fail to open file \"matranvuong.txt\" ";
		flag = 1;
	}
	fileKQ.open("ketqua.txt", ios::app);
	if (fileKQ.fail()){
		gotoxy(4,22); cout << "Fail to open file \"ketqua.txt\" ";
		flag = 1;
	}
	//mo file thanh cong
	if (flag == 0){
		fileKQ << "--------------------------------------------" << endl;
		fileKQ << "Tim nghich dao cua ma tran vuong: " << endl;
		file >> row >> col;
		//kiem tra ma tran vuong
		if (row != col){
			gotoxy(4,22); cout << "Ma tran khong vuong!" << endl;
			fileKQ << "Fail - Ma tran khong vuong!" << endl;
		}
		else{
			//lay cac phan tu cua ma tran tu file
			while(!file.eof()){
				file >> a[i][j]; 
				if (j < col-1)
					j++;
				else{
					i++;
					j = 0;
				}
			}
			fileKQ << "Ma tran A:" << endl;
			XuatMaTran(a, row, col);
			fileKQ << endl;
			//tao ma tran b = a
			for (i = 0; i < row; i++)
				for (j = 0; j < col; j++)
					b[i][j] = a[i][j];
			//kiem tra dinh thuc ma tran 
			if (Det(b, row) == 0){
				gotoxy(4,22); cout << "Det = 0, ma tran khong co nghich dao!" << endl;
				fileKQ << "Fail - Det = 0, ma tran khong co nghich dao!" << endl;
			}
			else{
				fileKQ << "Kiem tra dinh thuc ma tran: det = " << Det(b, row) << endl;
				fileKQ << endl;
				//while - chon PP thuc hien
				while(1){ 
					SetConsoleTextAttribute(hConsoleColor, 1);
					if (choice == 1)
						SetConsoleTextAttribute(hConsoleColor, 7);
					gotoxy(4,17); cout << "PP phan phu dai so" << endl;
					
					SetConsoleTextAttribute(hConsoleColor, 1);
					if (choice == 2)
						SetConsoleTextAttribute(hConsoleColor, 7);
					gotoxy(4,18); cout << "PP gauss jordan" << endl;
					//bat su kien tu ban phim
					key = getch();
					if (key == 72) // mui ten len
						if (choice == 1)
							choice = 2;
						else
							choice--;
					if (key == 80) // mui ten xuong
						if (choice == 2)
							choice = 1;
						else
							choice++;
					SetConsoleTextAttribute(hConsoleColor, 1);
					if (key == 13){ // phim enter
						break;
					}
				}
				//thuc hien PP vua chon
				switch(choice){
					case 1: 
						fileKQ << "PP phan phu dai so: " << endl;
						PhanPhuDaiSo(a, row); 
						break;
					case 2: 
						fileKQ << "PP Gauss Jordan: " << endl;
						GaussJordan(a, row); 
						break;
				}
			}
		}
	}
	
	file.close();
	fileKQ.close();
}
// ham bo tro - tim hang ma tran => phep khu Gauss
void TimHang(float a[][100], int r, int c){
	fstream fileKQ;
	int i = 0, j = 0, k, l, hang;
	float tmp;
	
	fileKQ.open("ketqua.txt", ios::app);
	
	while(i < r and j < c){
		//kiem tra phan tu dau khac 0
		if (a[i][j] == 0){
			for (k = i+1; k < r; k++)
				if (a[k][j] != 0){
					for (l = i; l < c; l++){
						tmp = a[i][l];
						a[i][l] = a[k][l];
						a[k][l] = tmp;
					}
					break;
				}
			if (k == r) // kiem tra xem cot do co full = 0 ?
				j++;
		}
		//thuc hien chuyen ve tam giac
		if (a[i][j] != 0){
			for (k = i+1; k < r; k++){
				tmp = (float)a[k][j]/(float)a[i][j]; 
				for (l = j; l < c; l++){
					a[k][l] -= a[i][l]*tmp; 
				}
			}
			i++;
			j++;
		}		
	}
	fileKQ << "Dua ve ma tran tam giac: " << endl;
	XuatMaTran(a, r, c);
	fileKQ << endl;
	hang = r; //khoi tao hang 
	for (i = 0; i < r; i++){
		for (j = 0; j < c; j++)
			if (a[i][j] != 0) //kiem tra hang co phan tu khac 0
				break;
		if (j == c) //neu hang khong co phan tu nao khac 0
			hang--;
	}
	fileKQ << "Ket qua: " << hang << endl;
	
	fileKQ.close();
}
//tim hang ma tran - Gauss
void TimHangMaTran(){
	fstream file, fileKQ;
	int row, col, i = 0, j = 0, hang, flag = 0;
	float a[100][100];
	
	//khoi tao mau - color
	HANDLE hConsoleColor;
	hConsoleColor = GetStdHandle(STD_OUTPUT_HANDLE);
			
	SetConsoleTextAttribute(hConsoleColor, 6);
	gotoxy(9,16); cout << "matrix1.txt";
	//mo file
	file.open("matrix1.txt", ios::in);
	if (file.fail()){
		gotoxy(4,22); cout << "Fail to open file \"matrix1.txt\" ";
		flag = 1;
	}
	fileKQ.open("ketqua.txt", ios::app);
	if (file.fail()){
		gotoxy(4,22); cout << "Fail to open file \"ketqua.txt\" ";
		flag = 1;
	}
	//mo file thanh cong
	if (flag == 0){
		fileKQ << "--------------------------------------" << endl;
		fileKQ << "Tim hang cua ma tran: " << endl;
		file >> row >> col;
		//lay cac phan tu cua ma tran tu file
		while(!file.eof()){
			file >> a[i][j]; 
			if (j < col-1)
				j++;
			else{
				i++;
				j = 0;
			}
		}
		fileKQ << "Ma tran: " << endl;
		XuatMaTran(a, row, col);
		fileKQ << endl;
		//tim hang thong qua function bo tro
		TimHang(a, row, col);
		//hien thi ra man hinh - thuc hien thanh cong
		SetConsoleTextAttribute(hConsoleColor, 4);
		gotoxy(4,22);  cout << "Complete!";
		gotoxy(4,23); cout << "Ket qua duoc luu vao file \"ketqua.txt\" ";
	}
	
	file.close();
	fileKQ.close();
	
}
//Ham bo tro - Tinh dinh thuc ma tran
double Det(float a[][100], int n){
	int i = 0, j = 0, k, l, hang, r, c;
	double tmp, det = 1;
	
	while(i < n and j < n){
		//kiem tra phan tu dau khac 0
		if (a[i][j] == 0){
			for (k = i+1; k < n; k++)
				if (a[k][j] != 0){
					for (l = i; l < n; l++){
						tmp = a[i][l];
						a[i][l] = a[k][l];
						a[k][l] = tmp;
					}
					break;
				}
			if (k == n) // kiem tra xem cot do co full = 0 ?
				j++;
		}
		//thuc hien chuyen ve tam giac
		if (a[i][j] != 0){
			for (k = i+1; k < n; k++){
				tmp = (float)a[k][j]/(float)a[i][j]; 
				for (l = j; l < n; l++){
					a[k][l] -= a[i][l]*tmp; 
				}
			}
			i++;
			j++;
		}				
	}
	for (i = 0; i < n; i++)
		det *= a[i][i];

	return det;
}
//Tim dinh thuc ma tran (goi ma tran tu file ra)
void TinhDinhThuc(){
	fstream file, fileKQ;
	int r, c, i = 0, j = 0, k, l, flag = 0;
	float a[100][100];
	double det = 1, tmp;
	
	//khoi tao mau - color
	HANDLE hConsoleColor;
	hConsoleColor = GetStdHandle(STD_OUTPUT_HANDLE);
	
	SetConsoleTextAttribute(hConsoleColor, 6);
	gotoxy(9,16); cout << "matranvuong.txt";
	//mo file
	file.open("matranvuong.txt", ios::in);
	if (file.fail()){
		gotoxy(4,22); cout << "Fail to open file \"matranvuong\" ";
		flag = 1;
	}
	fileKQ.open("ketqua.txt", ios::app);
	if (fileKQ.fail()){
		gotoxy(4,22); cout << "Fail to open file \"ketqua.txt\" ";
		flag = 1;
	}
	//mo file thanh cong
	if (flag == 0){
		fileKQ << "----------------------------------------------" << endl;
		fileKQ << "Tinh dinh thuc ma tran: " << endl;
		file >> r >> c;
		//kiem tra ma tran vuong
		if (r != c){
			gotoxy(4,22); cout << "Ma tran khong vuong - khong the tinh dinh thuc ma tran!" << endl;
			fileKQ << "Fail - Ma tran khong vuong!" << endl;
		}
		else{
			//lay ma tran tu file ra
			while (!file.eof()){
				file >> a[i][j];
				if (j < c-1)
					j++;
				else{
					i++;
					j = 0;
				}
			}
			fileKQ << "ma tran: " << endl;
			XuatMaTran(a, r, c);
			fileKQ << endl;
			i = 0;
			j = 0;
			while(i < r and j < c){
				//kiem tra phan tu dau khac 0
				if (a[i][j] == 0){
					for (k = i+1; k < r; k++)
						if (a[k][j] != 0){
							for (l = i; l < c; l++){
								tmp = a[i][l];
								a[i][l] = a[k][l];
								a[k][l] = tmp;
							}
							break;
						}
					if (k == r) // kiem tra xem cot do co full = 0 ?
						j++;
				}
				//thuc hien chuyen ve tam giac
				if (a[i][j] != 0){
					for (k = i+1; k < r; k++){
						tmp = (float)a[k][j]/(float)a[i][j]; 
						for (l = j; l < c; l++){
							a[k][l] -= a[i][l]*tmp; 
						}
					}
					i++;
					j++;
				}		
			}
			fileKQ << "Chuyen ma tran ve ma tran tam giac: " << endl;
			XuatMaTran(a, r, c);
			fileKQ << endl;
			//xuat ket qua - tich duong cheo
			fileKQ << "Tich duong cheo ma tran tam giac: " << endl;
			for (i = 0; i < r; i++)
				det *= a[i][i];
			fileKQ << "Ket qua: " << det << endl;
		}
		//hien thi ra man hinh - thuc hien thanh cong
		SetConsoleTextAttribute(hConsoleColor, 4);
		gotoxy(4,22);  cout << "Complete!";
		gotoxy(4,23); cout << "Ket qua duoc luu vao file \"ketqua.txt\" ";
	}
	
	file.close();
	fileKQ.close();
}
// bo tro tim tri rieng
void CreateMatrixM(float a[][100], float b[][100], int n, int row){
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			if (i != row){
				if (i == j)
					b[i][j] = 1;
				else
					b[i][j] = 0;
			}
			else{
				b[i][j] = a[row+1][j];
			}
}
void CreateMatrixM_1(float a[][100], float b[][100], int n, int row){
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			if (i != row){
				if (i == j)
					b[i][j] = 1;
				else
					b[i][j] = 0;
			}
			else{
				b[i][j] = -(a[row+1][j]/a[row+1][row]);
				if (j == row)
					if (b[i][j] != 0)
						b[i][j] = -b[i][j];
			}
}
// nhan hai ma tran vuong a,b -> tra ket qua ve ma tran c
void TichMaTran(float a[][100], float b[][100], float c[][100], int n){
	float tmp;
	for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++){
				tmp = 0;
				for (int k = 0; k < n; k++)
					tmp += a[i][k]*b[k][j];
				c[i][j] = tmp;
			}
}
// bo tro giai phuong trinh bac n
//f(x) - bo tro giai phuong trinh
float f(float x, float a[100], int n){
	float p = 0;
	for(int i = 0;i <= n; i++) 
		p = p*x + a[i];
	return p;
}
//f'(x) - bo tro giai phuong trinh
float fx(float x, float a[100], int n){
	float p = 0;
	for(int i = 0;i <= n-1; i++)
	p = p*x + n*a[i];
	return p;
}
//tim nghiem = PP lap - bo tro giai phuong trinh
float GiaiNghiem(float x, float a[100], int n, int &chot){
	int dem = 0, so = 10000;

	if(n == 1) // TH phuong trinh bac 1 
		return -(a[1]/a[0]);
	//thuc hien vong lap
	while (dem < so){
		if(dem == so - 1){
			if (fabs(f(x, a, n)) > 0.1){ //
				chot = 1;
				return 0;
			}
		return x;
		}
		x = x - f(x, a, n)/fx(x, a, n); // ct lap nghiem
		if(fabs(f(x, a, n)) < 0.00000000001) //kiem tra sai so cua nghiem x
			return x;
		dem++;
	}
	return chot=1;
}
// tim duoc nghiem, phan tich thanh nhan tu, giam bac phuong trinh - bo tro giai phuong trinh
void ChiaDaThuc(float x, float a[100], int &n){
	for(int i = 1;i < n; i++)
		a[i] = a[i] + a[i-1]*x;
	n = n-1;
}
// function giai phuong trinh bac n - bo tro tim tri rieng
void GiaiPhuongTrinh(float b[][100], int n){
	fstream fileKQ;
	double x;
	int ok = 0, i, chot;
	float a[100];
	
	//khoi tao mau - color
	HANDLE hConsoleColor;
	hConsoleColor = GetStdHandle(STD_OUTPUT_HANDLE);
	//mo file
	fileKQ.open("ketqua.txt", ios::app);
	if (fileKQ.fail()){
		gotoxy(4,22); cout << "Fail to open file \"ketqua.txt\" ";
	}
	else{
		fileKQ << "Ket qua: " << endl;
		// hang dau cua ma tran frobenius - la cac he so cua phuong trinh bac n
		a[0] = 1;
		for (i = 0; i < n; i++)
			a[i+1] = -b[0][i];
		//n++;	
		// giai tim cac nghiem - tri rieng
		while(n > 0){
			chot = 0;
			x = GiaiNghiem(0, a, n, chot); //tim nghiem
			if (chot == 1){ 
				if (ok == 0) //phuong trinh vo nghiem
					fileKQ << "Khong co tri rieng" << endl;
				break;
			}
			if (ok == 0) //phuong trinh co it nhat 1 nghiem - nghiem thu nhat
				fileKQ << "Cac tri rieng can tim la: " << endl;
			fileKQ << x << endl;
			ChiaDaThuc(x, a, n); // giam bac phuong trinh - chia cho nghiem vua tim duoc
			ok = 1; //danh dau phuong trinh co nghiem
		}
		//hien thi ra man hinh - thuc hien thanh cong
		SetConsoleTextAttribute(hConsoleColor, 4);
		gotoxy(4,22);  cout << "Complete!";
		gotoxy(4,23); cout << "Ket qua duoc luu vao file \"ketqua.txt\" ";
	}
	
	fileKQ.close();
}
// tim tri rieng bang phuong phap Danilevski - ma tran doi xung - ma tran Frobenius 
// cho truong hop li tuong- khong co phan tu 0 tai cheo
void TimTriRieng(){
	fstream file, fileKQ;
	float a[100][100], M[100][100], M_1[100][100], b[100][100];
	int i, j, m, n, k, flag = 0, step = 1;
	
	//khoi tao mau - color
	HANDLE hConsoleColor;
	hConsoleColor = GetStdHandle(STD_OUTPUT_HANDLE);
	
	SetConsoleTextAttribute(hConsoleColor, 6);
	gotoxy(9,16); cout << "matranvuong.txt";
	//mo file
	file.open("matranvuong.txt", ios::in);
	if (file.fail()){
		gotoxy(4,22); cout<<"Fail to open file \"matranvuong\" ";
		flag = 1;
	}
	fileKQ.open("ketqua.txt", ios::app);
	if (fileKQ.fail()){
		gotoxy(4,22); cout << "Fail to open file \"ketqua.txt\" ";
		flag = 1;
	}
	//mo file thanh cong
	if (flag == 0){
		fileKQ << "-------------------------------------------" << endl;
		fileKQ << "Tim tri rieng bang phuong phap Danilevski: " << endl;
		file >> m >> n;
		//kiem tra ma tran co vuong khong
		if (m != n){
			gotoxy(4,22); cout << "Ma tran khong vuong!" << endl;
			fileKQ << "Fail - Ma tran khong vuong!" << endl;
		}
		else{
			i = 0;
			j = 0;
			//lay ma tran tu file
			while(!file.eof()){
				file >> a[i][j]; 
				if (j < n-1)
					j++;
				else{
					i++;
					j = 0;
				}
			}
			fileKQ << "Ma tran: " << endl;
			XuatMaTran(a, n, n);
			fileKQ << endl;
			//PP danilevky
			fileKQ << "Dua ve ma tran Frobenius: " << endl;
			for (i = n-2; i >= 0; i--){
				fileKQ << "Lan " << step << ":" << endl;
				//chuyen ve ma tran Frobenius - ma tran tuong duong
				CreateMatrixM(a, M, n, i);
				fileKQ << "M: " << endl;
				XuatMaTran(M, n, n);
				//
				fileKQ << "M': " << endl;
				CreateMatrixM_1(a, M_1, n, i);
				XuatMaTran(M_1, n, n);
				//a = M*a*M_1
				fileKQ << "A" << step << " = M*A" << step-1 << "*M'" << endl;
				TichMaTran(M, a, b, n);
				TichMaTran(b, M_1, a, n);
				XuatMaTran(b, n, n);
				step++;
			}
			// tinh toan tim tri rieng - sau khi da dua ve ma tran Frobenius
			fileKQ << "Tri rieng x la nghiem cua phuong trinh det(A"<<step-1<<"-xE)=0 " << endl;
			GiaiPhuongTrinh(a, n);
		}
	}
	
	file.close();
	fileKQ.close();
}
// tim tri rieng bang phuong phap Danilevski - ma tran Frobenius - bo tro tim vecto rieng
void TriRieng(float b[][100], int n, float E[][100]){
	fstream fileKQ;
	double x;
	int ok = 0, i, chot, n1;
	float a[100];
	
	//khoi tao mau - color
	HANDLE hConsoleColor;
	hConsoleColor = GetStdHandle(STD_OUTPUT_HANDLE);
	//mo file
	fileKQ.open("ketqua.txt", ios::app);
	if (fileKQ.fail()){
		gotoxy(4,22); cout << "Fail to open file \"ketqua.txt\" ";
	}
	else{
		// hang dau cua ma tran frobenius - la cac he so cua phuong trinh bac n
		a[0] = 1;
		for (i = 0; i < n; i++)
			a[i+1] = -b[0][i];
		//n++;	
		// giai tim cac nghiem - tri rieng
		n1 = n;
		while(n > 0){
			chot = 0;
			x = GiaiNghiem(0, a, n, chot);
			if (chot == 1){
				if (ok == 0) //phuong trinh vo nghiem
					fileKQ << "Khong co tri rieng!" << endl;
				break;
			}
			if (ok == 0){ //phuong trinh co it nhat 1 nghiem
				fileKQ << "B2. tim vecto rieng tuong ung voi cac tri rieng: " << endl;
				fileKQ << "M: " << endl;
				XuatMaTran(E, n, n);
				fileKQ << endl;
			}
			fileKQ << "Tri rieng = " << x << endl;
			VectoRieng(x, n1, E); //tinh vecto tuong ung tri rieng
			ChiaDaThuc(x, a, n); //chia phuong trinh cho nghiem vua tim duoc
			ok = 1; //danh giau phuong trinh co nghiem
		}
		//hien thi ra man hinh - thuc hien thanh cong
		SetConsoleTextAttribute(hConsoleColor, 4);
		gotoxy(4,22);  cout << "Complete!";
		gotoxy(4,23); cout << "Ket qua duoc luu vao file \"ketqua.txt\" ";
	}
	
	fileKQ.close();
}
//function tim vecto rieng tuong ung - bo tro tim vecto rieng
void VectoRieng(float x, int n, float E[][100]){
	fstream fileKQ;
	float a[100][100], b[100];
	int i, j, k;
	float tmp;
	//mo file
	fileKQ.open("ketqua.txt", ios::app);
	if (fileKQ.fail()){
		gotoxy(4,22); cout << "Fail to open file \"ketqua.txt\" ";
	}
	else{
		//tao vecto rieng cua ma tran frobenius
		a[n-1][0] = 1;
		for (i = n-2; i >= 0; i--){
			a[i][0] = a[i+1][0] * x;
		}
		fileKQ << "vecto rieng cua ma tran Frobenius: " << endl;
		fileKQ << "y = (";
		for (i = 0; i < n-1; i++)
			fileKQ << a[i][0] << ", ";
		fileKQ << a[n-1][0] << ")" << endl;
		//tinh ma tran M - truyen ma tran E
		for (i = 0; i < n; i++){
			tmp = 0;
			for (j = 0; j < n; j++)
				tmp += E[i][j] * a[j][0];
			b[i] = tmp;
		}
		//hien thi vecto ra fileKQ
		fileKQ << "Vecto rieng tuong ung: " << endl;
		fileKQ << "v = M*y" << endl;
		fileKQ << "Ket qua: " << endl;
		fileKQ << "v = (";
		for (i = 0; i < n-1; i++)
			fileKQ << b[i] << ", ";
		fileKQ << b[n-1] << ")" << endl;
		fileKQ << endl;
	}
	
	fileKQ.close();
}
// Tim vecto rieng - main
void TimVectoRieng(){
	fstream file, fileKQ;
	float a[100][100], M[100][100], M_1[100][100], b[100][100], E[100][100], E1[100][100];
	int m, n, i, j, k, flag = 0, step = 1;
	
	//khoi tao mau - color
	HANDLE hConsoleColor;
	hConsoleColor = GetStdHandle(STD_OUTPUT_HANDLE);
	
	SetConsoleTextAttribute(hConsoleColor, 6);
	gotoxy(8,16); cout << "matranvuong.txt";
	//mo file
	file.open("matranvuong.txt", ios::in);
	if (file.fail()){
		gotoxy(4,22); cout<<"Fail to open file \"matranvuong.txt\" ";
		flag = 1;
	}
	fileKQ.open("ketqua.txt", ios::app);
	if (fileKQ.fail()){
		gotoxy(4,22); cout << "Fail to open file \"ketqua.txt\" ";
		flag = 1;
	}
	//mo file thanh cong
	if (flag == 0){
		fileKQ << "---------------------------------------------" << endl;
		fileKQ << "Tim vecto rieng bang phuong phap Danilevski: " << endl;
		file >> m >> n;
		//kiem tra ma tran vuong
		if (m != n){
			gotoxy(4,22); cout << "Ma tran khong vuong!" << endl;
			fileKQ << "Fail - Ma tran khong vuong!" << endl;
		}
		else{
			i = 0;
			j = 0;
			//lay ma tran tu file
			while(!file.eof()){
				file >> a[i][j]; 
				if (j < n-1)
					j++;
				else{
					i++;
					j = 0;
				}
			}
			fileKQ << "Ma tran: " << endl;
			XuatMaTran(a, n, n);
			fileKQ << endl;
			//tao ma tran E - ma tran don vi
			for (i = 0; i < n; i++)
				for (j = 0; j < n; j++)
					if (i == j)
						E[i][j] = 1;
					else
						E[i][j] = 0;
			//PP danilevsky
			fileKQ << "B1. tim tri rieng" << endl;
			fileKQ << "Dua ve ma tran Frobenius: " << endl;
			for (i = n-2; i >= 0; i--){
				fileKQ << "Lan " << step << ":" << endl;
				//chuyen ve ma tran Frobenius - ma tran tuong duong
				CreateMatrixM(a, M, n, i);		
				fileKQ << "M: " << endl;
				XuatMaTran(M, n, n);
				//
				CreateMatrixM_1(a, M_1, n, i);
				fileKQ << "M': " << endl;
				XuatMaTran(M_1, n, n);
				//tao ma tran M
				TichMaTran(E, M_1, E1, n);
				for (j = 0; j < n; j++)
					for (k = 0; k < n; k++)
						E[j][k] = E1[j][k];
				// A = M*A*M_1
				fileKQ << "A" << step << " = M*A" << step-1 << "*M'" << endl;
				TichMaTran(M, a, b, n);
				TichMaTran(b, M_1, a, n);
				XuatMaTran(b, n, n);
				step++;
			}
			// tinh toan tim tri rieng
			TriRieng(a, n, E);
		}
	}
	
	file.close();
	fileKQ.close();
}
