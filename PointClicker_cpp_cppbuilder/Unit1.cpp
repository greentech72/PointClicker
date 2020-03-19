//---------------------------------------------------------------------------

#include <vcl.h>
#pragma hdrstop

#include "Unit1.h"
//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma resource "*.dfm"
TForm1 *Form1;
//---------------------------------------------------------------------------
__fastcall TForm1::TForm1(TComponent* Owner)
	: TForm(Owner)
{
string* u = pcg.get_upgrades();
string* ud = pcg.get_upgrades_description();
unsigned long long* uc = pcg.get_upgrades_cost();
unsigned long long* ua = pcg.get_upgrades_amount();

/*
for (int i = 0; i < pcg.upgrades_capacity; i++) {
		cout << setw(20) << i + 1 << ") [" << ua[i] << "] " << u[i] << " " << ud[i] << " It'll cost : " << uc[i] << endl;
}
*/
pcg.load();
for(int i = 1; i < pcg.upgrades_capacity; i++){
	ListBox1->Items->Add( (u[i] + " " + std::to_string(uc[i]) + " [" + std::to_string(ua[i]) + "]" ).c_str() );
}

}
//---------------------------------------------------------------------------
void __fastcall TForm1::Button2Click(TObject *Sender)
{
pcg.save();
Form1->Close();
}
//---------------------------------------------------------------------------
void __fastcall TForm1::Timer1Timer(TObject *Sender)
{
Label1->Caption = ("Score : " + std::to_string(pcg.get_score())).c_str();
Label2->Caption = ("PPS : " + std::to_string(pcg.get_pps())).c_str();
pcg.add_pps();
}
//---------------------------------------------------------------------------
void __fastcall TForm1::Button1Click(TObject *Sender)
{
pcg.command(0);
}
//---------------------------------------------------------------------------
