// Decompiled with JetBrains decompiler
// Type: Inkie.Form1
// Assembly: void, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
// MVID: 6375A302-8B89-4390-988B-27B32CB1C78F
// Assembly location: C:\Users\Manzel\Desktop\Oh_No_Find_The_Key.exe

using System;
using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;

namespace Inkie
{
  public class Form1 : Form
  {
    private IContainer components;
    private Label label1;
    private TextBox txtPass;
    private Button btnCheck;
    private Label label2;
    private Label label3;
    private Label label4;
    private Label label5;

    public Form1()
    {
      this.InitializeComponent();
    }

    private string reverse(string original)
    {
      char[] charArray = original.ToCharArray();
      Array.Reverse((Array) charArray);
      return new string(charArray);
    }

    private bool ShallHePass()
    {
      return this.txtPass.Text == this.reverse(this.label2.Text + this.label3.Text + this.label4.Text + this.label5.Text);
    }

    private void btnCheck_Click(object sender, EventArgs e)
    {
      this.label3.Text = "FGSfVWTf";
      int num = (int) MessageBox.Show(this.ShallHePass() ? "you got the encrypted flag" : "Try Again Hacker xD !");
    }

    private void Form1_Load(object sender, EventArgs e)
    {
      this.label4.Text = "Rmb19mRfV3b";
    }

    protected override void Dispose(bool disposing)
    {
      if (disposing && this.components != null)
        this.components.Dispose();
      base.Dispose(disposing);
    }

    private void InitializeComponent()
    {
      this.label1 = new Label();
      this.txtPass = new TextBox();
      this.btnCheck = new Button();
      this.label2 = new Label();
      this.label3 = new Label();
      this.label4 = new Label();
      this.label5 = new Label();
      this.SuspendLayout();
      this.label1.AutoSize = true;
      this.label1.Location = new Point(12, 80);
      this.label1.Name = "label1";
      this.label1.Size = new Size(131, 13);
      this.label1.TabIndex = 0;
      this.label1.Text = "Anokha CTF Key";
      this.txtPass.Location = new Point(143, 77);
      this.txtPass.Name = "txtPass";
      this.txtPass.Size = new Size(129, 20);
      this.txtPass.TabIndex = 1;
      this.btnCheck.Location = new Point(105, 125);
      this.btnCheck.Name = "btnCheck";
      this.btnCheck.Size = new Size(75, 23);
      this.btnCheck.TabIndex = 2;
      this.btnCheck.Text = "I shall Pass!";
      this.btnCheck.UseVisualStyleBackColor = true;
      this.btnCheck.Click += new EventHandler(this.btnCheck_Click);
      this.label2.AutoSize = true;
      this.label2.ForeColor = SystemColors.Control;
      this.label2.Location = new Point(12, 165);
      this.label2.Name = "label2";
      this.label2.Size = new Size(55, 13);
      this.label2.TabIndex = 3;
      this.label2.Text = "==QfyV2aj";
      this.label3.AutoSize = true;
      this.label3.ForeColor = SystemColors.Control;
      this.label3.Location = new Point(12, 178);
      this.label3.Name = "label3";
      this.label3.Size = new Size(55, 13);
      this.label3.TabIndex = 4;
      this.label4.AutoSize = true;
      this.label4.ForeColor = SystemColors.Control;
      this.label4.Location = new Point(12, 191);
      this.label4.Name = "label4";
      this.label4.Size = new Size(53, 13);
      this.label4.TabIndex = 5;
      this.label5.AutoSize = true;
      this.label5.ForeColor = SystemColors.Control;
      this.label5.Location = new Point(12, 204);
      this.label5.Name = "label5";
      this.label5.Size = new Size(54, 13);
      this.label5.TabIndex = 6;
      this.label5.Text = "ZtXYyFWbvlGe";
      this.AutoScaleDimensions = new SizeF(6f, 13f);
      this.AutoScaleMode = AutoScaleMode.Font;
      this.ClientSize = new Size(284, 262);
      this.Controls.Add((Control) this.label5);
      this.Controls.Add((Control) this.label4);
      this.Controls.Add((Control) this.label3);
      this.Controls.Add((Control) this.label2);
      this.Controls.Add((Control) this.btnCheck);
      this.Controls.Add((Control) this.txtPass);
      this.Controls.Add((Control) this.label1);
      this.FormBorderStyle = FormBorderStyle.FixedSingle;
      this.MaximizeBox = false;
      this.MinimizeBox = false;
      this.Name = nameof (Form1);
      this.Text = " Xiomara CTF Key:";
      this.Load += new EventHandler(this.Form1_Load);
      this.ResumeLayout(false);
      this.PerformLayout();
    }
  }
}
