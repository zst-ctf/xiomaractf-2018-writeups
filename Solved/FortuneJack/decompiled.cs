// Decompiled with JetBrains decompiler
// Type: XiomaraChallenge.Form1
// Assembly: XiomaraChallenge, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
// MVID: 39B24F62-7744-4BAB-A6AB-AA43BEBD499B
// Assembly location: C:\Users\Manzel\Desktop\Lucky_Drawer.exe

using System;
using System.ComponentModel;
using System.Drawing;
using System.Security.Cryptography;
using System.Text;
using System.Windows.Forms;

namespace XiomaraChallenge
{
  public class Form1 : Form
  {
    private IContainer components = (IContainer) null;
    private Label label1;
    private Button button1;
    private PictureBox pictureBox1;
    private Label label2;
    private Label label3;

    public Form1()
    {
      this.InitializeComponent();
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

    private void checkflag(int key)
    {
      StringBuilder stringBuilder = new StringBuilder();
      string str1 = "xiomara{";
      string str2 = "þæþÖîûìèýÖðæüÖíàíÖàýÖ\x00B3 ";
      string str3 = "}";
      string str4 = "DB2C17E69713C8604A91AA7A51CBA041";
      for (int index = 0; index < str2.Length; ++index)
        stringBuilder.Append((char) ((uint) str2[index] ^ (uint) key));
      string input = stringBuilder.ToString();
      string md5 = Form1.CreateMD5(input);
      if (md5.Equals(str4))
      {
        this.label3.Text = str1 + input + str3;
        this.label3.Visible = true;
      }
      if (!(md5 != str4))
        return;
      this.label3.Text = "Sorry You are Not So Lucky :(  OH!";
      this.label3.Visible = true;
    }

    private void button1_Click(object sender, EventArgs e)
    {
      this.pictureBox1.Visible = true;
      int key = new Random().Next(1500);
      this.label2.Text = key.ToString();
      this.label2.Visible = true;
      this.checkflag(key);
    }

    private void label2_Click(object sender, EventArgs e)
    {
    }

    private void label3_Click(object sender, EventArgs e)
    {
    }

    protected override void Dispose(bool disposing)
    {
      if (disposing && this.components != null)
        this.components.Dispose();
      base.Dispose(disposing);
    }

    private void InitializeComponent()
    {
      ComponentResourceManager componentResourceManager = new ComponentResourceManager(typeof (Form1));
      this.label1 = new Label();
      this.button1 = new Button();
      this.pictureBox1 = new PictureBox();
      this.label2 = new Label();
      this.label3 = new Label();
      ((ISupportInitialize) this.pictureBox1).BeginInit();
      this.SuspendLayout();
      this.label1.AutoSize = true;
      this.label1.Location = new Point(26, 310);
      this.label1.Name = "label1";
      this.label1.Size = new Size(148, 13);
      this.label1.TabIndex = 1;
      this.label1.Text = "Generate Your Lucky Number";
      this.button1.Location = new Point(185, 305);
      this.button1.Name = "button1";
      this.button1.Size = new Size(75, 23);
      this.button1.TabIndex = 2;
      this.button1.Text = "Generate";
      this.button1.UseVisualStyleBackColor = true;
      this.button1.Click += new EventHandler(this.button1_Click);
      this.pictureBox1.Image = (Image) componentResourceManager.GetObject("pictureBox1.Image");
      this.pictureBox1.Location = new Point(89, 25);
      this.pictureBox1.Name = "pictureBox1";
      this.pictureBox1.Size = new Size(291, 248);
      this.pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;
      this.pictureBox1.TabIndex = 3;
      this.pictureBox1.TabStop = false;
      this.pictureBox1.Visible = false;
      this.label2.AutoSize = true;
      this.label2.BackColor = SystemColors.GradientActiveCaption;
      this.label2.Font = new Font("Times New Roman", 18f, FontStyle.Bold, GraphicsUnit.Point, (byte) 0);
      this.label2.Location = new Point(212, 134);
      this.label2.Name = "label2";
      this.label2.Size = new Size(74, 26);
      this.label2.TabIndex = 4;
      this.label2.Text = "label2";
      this.label2.Visible = false;
      this.label2.Click += new EventHandler(this.label2_Click);
      this.label3.AutoSize = true;
      this.label3.Font = new Font("Monotype Corsiva", 14.25f, FontStyle.Italic, GraphicsUnit.Point, (byte) 0);
      this.label3.Location = new Point(123, 276);
      this.label3.Name = "label3";
      this.label3.Size = new Size(51, 22);
      this.label3.TabIndex = 5;
      this.label3.Text = "label3";
      this.label3.Visible = false;
      this.label3.Click += new EventHandler(this.label3_Click);
      this.AutoScaleDimensions = new SizeF(6f, 13f);
      this.AutoScaleMode = AutoScaleMode.Font;
      this.BackColor = Color.LightGray;
      this.BackgroundImage = (Image) componentResourceManager.GetObject("$this.BackgroundImage");
      this.ClientSize = new Size(485, 355);
      this.Controls.Add((Control) this.label3);
      this.Controls.Add((Control) this.label2);
      this.Controls.Add((Control) this.button1);
      this.Controls.Add((Control) this.label1);
      this.Controls.Add((Control) this.pictureBox1);
      this.ForeColor = SystemColors.ControlText;
      this.Name = nameof (Form1);
      this.RightToLeft = RightToLeft.No;
      this.Text = nameof (Form1);
      ((ISupportInitialize) this.pictureBox1).EndInit();
      this.ResumeLayout(false);
      this.PerformLayout();
    }
  }
}
