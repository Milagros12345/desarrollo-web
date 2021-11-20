#include<bits/stdc++.h>
using namespace std;

int matrix[4][4]={{43,163,89,139},
                  {197,41,127,53},
                  {97,103,31,113},
                  {211,13,151,19}};
int estado[4][16]={
  {43,161,366,234,67,204,336,306,298,188,135,287,199,113,13,95},
  {211,52,264,155,278,322,155,294,46,218,275,236,396,197,33,321},
  {87,344,280,163,111,19,151,395,102,77,104,184,28,184,302,69},
  {44,230,350,200,245,94,56,366,282,89,225,202,393,117,242,190}};
int generar_aleatorio(int n){
  int num= 2 + rand()%(n -2);
  return num;
}
bool esPrimo(int x) {
  int primos=0;
  for(int i = 1;i <= x; ++i){
		if (x%i == 0 )
			++primos;	
	}
	return (primos == 2);
}
int gen_prime(int n){
  int num= generar_aleatorio(n);
  while(!esPrimo(num)){
    num= generar_aleatorio(n);
  }
  return num;
}
string int_to_string(int number, int digits){
  string ans = "";
  while (number) {
    ans.push_back('0'+ (number % 10));
    number /= 10;
  }
  reverse(ans.begin(), ans.end());
  return string(digits - ans.size(), '0') + ans;
}
string to_string(int abc){
    string str;
    stringstream ss;  
    ss << abc;  
    ss >> str;
    return str;
}
class Aes{
    string msg;
    string alf="+abcdefghijkmnopqrstuvwxyz.-*";
    int matrixmsg[4][4];//si es vacio completar con 0
public:
    Aes(){};
    int pos(char s,string m){
      int x=0;
      for(int i=0;i<m.size();i++){
        if(s==m[i]){
          x=i;break;
        }
      }return x;
    }
  
    void suma(int s[4][16],int mat[4][4]){
      for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
          mat[i][j]=matrix[i][j] + s[i][j+4];
        }
      }
    }
    void combinar(int matrix[4][4], int a[4][4]){
      int tmp[4][4],tmp2[4][4];
      suma(estado,tmp);
      for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
          tmp2[i][j]= tmp[i][j] xor matrixmsg[i][j];
        }
      }
      a=tmp2;
    }
    void row(int m[4][4]){
      for(int i=0;i<4;i++){
        swap(m[i][0],m[i][3]);
      }
    }
    
    string cifrado(string msg_){
      msg=msg_;
      int x=0;
      for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
          if(x<msg.size()){
            matrixmsg[i][j]=pos(msg[x],msg);
          }
          else{
            matrixmsg[i][j]=0;
          }
        }
      }
      int ds[4][4];
      combinar(matrix,ds);
      row(ds);
      string abc;
      for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
          abc+= int_to_string(15,ds[i][j]);
        }
      }
      return abc;
    }
};
int main(){
  Aes r;
  string msg="hola";
  cout<<endl<<r.cifrado(msg)<<endl;
  return 0;
}