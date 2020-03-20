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

pcg.load();
/*for(int i = 1; i < pcg.upgrades_capacity; i++){
	ListBox1->Items->Add( (u[i] + " " + std::to_string(uc[i]) + " [" + std::to_string(ua[i]) + "]" ).c_str() );
} */
SHOW();
}
//---------------------------------------------------------------------------
void __fastcall TForm1::Button2Click(TObject *Sender)
{
pcg.save();
Form1->Close();
}
//---------------------------------------------------------------------------
void __fastcall TForm1::SHOW(){
string* u = pcg.get_upgrades();
//string* ud = pcg.get_upgrades_description();
unsigned long long* uc = pcg.get_upgrades_cost();
unsigned long long* ua = pcg.get_upgrades_amount();
for(int i = 1; i < pcg.upgrades_capacity; i++){
	ListBox1->Items->Add( (u[i] + " " + std::to_string(uc[i]) + " [" + std::to_string(ua[i]) + "]" ).c_str() );
    //ListBox1->ItemsHint[i] = ud[i].c_str();
}
}
void __fastcall TForm1::Timer1Timer(TObject *Sender)
{
Label1->Caption = ("Score : " + std::to_string(pcg.get_score())).c_str();
Label2->Caption = ("PPS : " + std::to_string(pcg.get_pps())).c_str();
//SHOW();
pcg.add_pps();
}
//---------------------------------------------------------------------------
void __fastcall TForm1::Button1Click(TObject *Sender)
{
pcg.command(0);
}
//---------------------------------------------------------------------------
void __fastcall TForm1::ListBox1Click(TObject *Sender)
{
int sel = ListBox1->ItemIndex;
pcg.command(sel + 1);
ListBox1->Clear();
SHOW();
Timer2->Enabled = true;
string* ud = pcg.get_upgrades_description();
Label3->Caption = ud[sel+1].c_str();
}
//---------------------------------------------------------------------------

void __fastcall TForm1::Timer2Timer(TObject *Sender)
{
Label3->Caption = "";
Timer2->Enabled = false;
}
//---------------------------------------------------------------------------

void __fastcall TForm1::Exit1Click(TObject *Sender)
{
Form1->Close();
}
//---------------------------------------------------------------------------

void __fastcall TForm1::Save1Click(TObject *Sender)
{
pcg.save();
Timer2->Enabled = true;
Label3->Caption = "Saved...";
}
//---------------------------------------------------------------------------

void __fastcall TForm1::Load1Click(TObject *Sender)
{
pcg.load();
Timer2->Enabled = true;
Label3->Caption = "Loaded...";
}
//---------------------------------------------------------------------------

