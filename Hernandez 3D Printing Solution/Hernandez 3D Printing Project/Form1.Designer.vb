<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class Form1
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.Label1 = New System.Windows.Forms.Label()
        Me.ListBox1 = New System.Windows.Forms.ListBox()
        Me.TextBox1 = New System.Windows.Forms.TextBox()
        Me.radFree = New System.Windows.Forms.RadioButton()
        Me.rad2 = New System.Windows.Forms.RadioButton()
        Me.radNext = New System.Windows.Forms.RadioButton()
        Me.Label2 = New System.Windows.Forms.Label()
        Me.calcButton = New System.Windows.Forms.Button()
        Me.Gtotalbox = New System.Windows.Forms.TextBox()
        Me.taxbox = New System.Windows.Forms.TextBox()
        Me.shipbox = New System.Windows.Forms.TextBox()
        Me.subbox = New System.Windows.Forms.TextBox()
        Me.Label3 = New System.Windows.Forms.Label()
        Me.Label4 = New System.Windows.Forms.Label()
        Me.Label5 = New System.Windows.Forms.Label()
        Me.Label6 = New System.Windows.Forms.Label()
        Me.taxboxLabel = New System.Windows.Forms.Label()
        Me.shipboxLabel = New System.Windows.Forms.Label()
        Me.Label9 = New System.Windows.Forms.Label()
        Me.cboMaterial = New System.Windows.Forms.ComboBox()
        Me.SuspendLayout()
        '
        'Label1
        '
        Me.Label1.AutoSize = True
        Me.Label1.Font = New System.Drawing.Font("Segoe Script", 27.75!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label1.Location = New System.Drawing.Point(41, -4)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(524, 61)
        Me.Label1.TabIndex = 0
        Me.Label1.Text = "Hernandez 3D Printing "
        '
        'ListBox1
        '
        Me.ListBox1.BackColor = System.Drawing.SystemColors.ButtonFace
        Me.ListBox1.BorderStyle = System.Windows.Forms.BorderStyle.None
        Me.ListBox1.FormattingEnabled = True
        Me.ListBox1.Items.AddRange(New Object() {"Material" & Global.Microsoft.VisualBasic.ChrW(9) & Global.Microsoft.VisualBasic.ChrW(9) & "Part cost" & Global.Microsoft.VisualBasic.ChrW(9) & Global.Microsoft.VisualBasic.ChrW(9) & "Material cost", "", "Plastic" & Global.Microsoft.VisualBasic.ChrW(9) & Global.Microsoft.VisualBasic.ChrW(9) & "$1.50" & Global.Microsoft.VisualBasic.ChrW(9) & Global.Microsoft.VisualBasic.ChrW(9) & "$0.27/cm", "", "Metallic Plastic" & Global.Microsoft.VisualBasic.ChrW(9) & "$1.50" & Global.Microsoft.VisualBasic.ChrW(9) & Global.Microsoft.VisualBasic.ChrW(9) & "$0.57/cm", "", "Stainless Steel" & Global.Microsoft.VisualBasic.ChrW(9) & "$6.00" & Global.Microsoft.VisualBasic.ChrW(9) & Global.Microsoft.VisualBasic.ChrW(9) & "$5.00/cm"})
        Me.ListBox1.Location = New System.Drawing.Point(52, 78)
        Me.ListBox1.Name = "ListBox1"
        Me.ListBox1.Size = New System.Drawing.Size(276, 91)
        Me.ListBox1.TabIndex = 1
        '
        'TextBox1
        '
        Me.TextBox1.Location = New System.Drawing.Point(446, 139)
        Me.TextBox1.Name = "TextBox1"
        Me.TextBox1.Size = New System.Drawing.Size(119, 20)
        Me.TextBox1.TabIndex = 3
        '
        'radFree
        '
        Me.radFree.AutoSize = True
        Me.radFree.Location = New System.Drawing.Point(419, 182)
        Me.radFree.Name = "radFree"
        Me.radFree.Size = New System.Drawing.Size(46, 17)
        Me.radFree.TabIndex = 4
        Me.radFree.TabStop = True
        Me.radFree.Text = "Free"
        Me.radFree.UseVisualStyleBackColor = True
        '
        'rad2
        '
        Me.rad2.AutoSize = True
        Me.rad2.Location = New System.Drawing.Point(471, 175)
        Me.rad2.Name = "rad2"
        Me.rad2.Size = New System.Drawing.Size(55, 30)
        Me.rad2.TabIndex = 5
        Me.rad2.TabStop = True
        Me.rad2.Text = "2-Day" & Global.Microsoft.VisualBasic.ChrW(13) & Global.Microsoft.VisualBasic.ChrW(10) & "$7.50 "
        Me.rad2.UseVisualStyleBackColor = True
        '
        'radNext
        '
        Me.radNext.AutoSize = True
        Me.radNext.Location = New System.Drawing.Point(532, 175)
        Me.radNext.Name = "radNext"
        Me.radNext.Size = New System.Drawing.Size(69, 30)
        Me.radNext.TabIndex = 6
        Me.radNext.TabStop = True
        Me.radNext.Text = "Next-Day" & Global.Microsoft.VisualBasic.ChrW(13) & Global.Microsoft.VisualBasic.ChrW(10) & "$16.00"
        Me.radNext.UseVisualStyleBackColor = True
        '
        'Label2
        '
        Me.Label2.AutoSize = True
        Me.Label2.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.25!, CType((System.Drawing.FontStyle.Bold Or System.Drawing.FontStyle.Underline), System.Drawing.FontStyle), System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label2.Location = New System.Drawing.Point(353, 57)
        Me.Label2.Name = "Label2"
        Me.Label2.Size = New System.Drawing.Size(75, 13)
        Me.Label2.TabIndex = 7
        Me.Label2.Text = "Select your:"
        '
        'calcButton
        '
        Me.calcButton.Location = New System.Drawing.Point(462, 211)
        Me.calcButton.Name = "calcButton"
        Me.calcButton.Size = New System.Drawing.Size(75, 23)
        Me.calcButton.TabIndex = 8
        Me.calcButton.Text = "Calculate"
        Me.calcButton.UseVisualStyleBackColor = True
        '
        'Gtotalbox
        '
        Me.Gtotalbox.Location = New System.Drawing.Point(410, 271)
        Me.Gtotalbox.Name = "Gtotalbox"
        Me.Gtotalbox.Size = New System.Drawing.Size(100, 20)
        Me.Gtotalbox.TabIndex = 9
        '
        'taxbox
        '
        Me.taxbox.Location = New System.Drawing.Point(291, 271)
        Me.taxbox.Name = "taxbox"
        Me.taxbox.Size = New System.Drawing.Size(100, 20)
        Me.taxbox.TabIndex = 10
        '
        'shipbox
        '
        Me.shipbox.Location = New System.Drawing.Point(172, 271)
        Me.shipbox.Name = "shipbox"
        Me.shipbox.Size = New System.Drawing.Size(100, 20)
        Me.shipbox.TabIndex = 11
        '
        'subbox
        '
        Me.subbox.Location = New System.Drawing.Point(52, 271)
        Me.subbox.Name = "subbox"
        Me.subbox.Size = New System.Drawing.Size(100, 20)
        Me.subbox.TabIndex = 12
        '
        'Label3
        '
        Me.Label3.AutoSize = True
        Me.Label3.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.25!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label3.Location = New System.Drawing.Point(353, 91)
        Me.Label3.Name = "Label3"
        Me.Label3.Size = New System.Drawing.Size(52, 13)
        Me.Label3.TabIndex = 13
        Me.Label3.Text = "Material"
        '
        'Label4
        '
        Me.Label4.AutoSize = True
        Me.Label4.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.25!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label4.Location = New System.Drawing.Point(353, 139)
        Me.Label4.Name = "Label4"
        Me.Label4.Size = New System.Drawing.Size(48, 13)
        Me.Label4.TabIndex = 14
        Me.Label4.Text = "Volume"
        '
        'Label5
        '
        Me.Label5.AutoSize = True
        Me.Label5.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.25!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label5.Location = New System.Drawing.Point(353, 175)
        Me.Label5.Name = "Label5"
        Me.Label5.Size = New System.Drawing.Size(60, 26)
        Me.Label5.TabIndex = 15
        Me.Label5.Text = "Shipping " & Global.Microsoft.VisualBasic.ChrW(13) & Global.Microsoft.VisualBasic.ChrW(10) & " Method"
        '
        'Label6
        '
        Me.Label6.AutoSize = True
        Me.Label6.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.25!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label6.Location = New System.Drawing.Point(72, 255)
        Me.Label6.Name = "Label6"
        Me.Label6.Size = New System.Drawing.Size(58, 13)
        Me.Label6.TabIndex = 16
        Me.Label6.Text = "SubTotal"
        '
        'taxboxLabel
        '
        Me.taxboxLabel.AutoSize = True
        Me.taxboxLabel.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.25!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.taxboxLabel.Location = New System.Drawing.Point(323, 255)
        Me.taxboxLabel.Name = "taxboxLabel"
        Me.taxboxLabel.Size = New System.Drawing.Size(28, 13)
        Me.taxboxLabel.TabIndex = 17
        Me.taxboxLabel.Text = "Tax"
        '
        'shipboxLabel
        '
        Me.shipboxLabel.AutoSize = True
        Me.shipboxLabel.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.25!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.shipboxLabel.Location = New System.Drawing.Point(187, 255)
        Me.shipboxLabel.Name = "shipboxLabel"
        Me.shipboxLabel.Size = New System.Drawing.Size(85, 13)
        Me.shipboxLabel.TabIndex = 18
        Me.shipboxLabel.Text = "Shipping Cost"
        '
        'Label9
        '
        Me.Label9.AutoSize = True
        Me.Label9.Font = New System.Drawing.Font("Microsoft Sans Serif", 8.25!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label9.Location = New System.Drawing.Point(425, 255)
        Me.Label9.Name = "Label9"
        Me.Label9.Size = New System.Drawing.Size(74, 13)
        Me.Label9.TabIndex = 19
        Me.Label9.Text = "Grand Total"
        '
        'cboMaterial
        '
        Me.cboMaterial.FormattingEnabled = True
        Me.cboMaterial.Location = New System.Drawing.Point(444, 91)
        Me.cboMaterial.Name = "cboMaterial"
        Me.cboMaterial.Size = New System.Drawing.Size(121, 21)
        Me.cboMaterial.TabIndex = 20
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(613, 303)
        Me.Controls.Add(Me.cboMaterial)
        Me.Controls.Add(Me.Label9)
        Me.Controls.Add(Me.shipboxLabel)
        Me.Controls.Add(Me.taxboxLabel)
        Me.Controls.Add(Me.Label6)
        Me.Controls.Add(Me.Label5)
        Me.Controls.Add(Me.Label4)
        Me.Controls.Add(Me.Label3)
        Me.Controls.Add(Me.subbox)
        Me.Controls.Add(Me.shipbox)
        Me.Controls.Add(Me.taxbox)
        Me.Controls.Add(Me.Gtotalbox)
        Me.Controls.Add(Me.calcButton)
        Me.Controls.Add(Me.Label2)
        Me.Controls.Add(Me.radNext)
        Me.Controls.Add(Me.rad2)
        Me.Controls.Add(Me.radFree)
        Me.Controls.Add(Me.TextBox1)
        Me.Controls.Add(Me.ListBox1)
        Me.Controls.Add(Me.Label1)
        Me.Name = "Form1"
        Me.Text = "Hernandez 3D Printing Calculator"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub

    Friend WithEvents Label1 As Label
    Friend WithEvents ListBox1 As ListBox
    Friend WithEvents TextBox1 As TextBox
    Friend WithEvents radFree As RadioButton
    Friend WithEvents rad2 As RadioButton
    Friend WithEvents radNext As RadioButton
    Friend WithEvents Label2 As Label
    Friend WithEvents calcButton As Button
    Friend WithEvents Gtotalbox As TextBox
    Friend WithEvents taxbox As TextBox
    Friend WithEvents shipbox As TextBox
    Friend WithEvents subbox As TextBox
    Friend WithEvents Label3 As Label
    Friend WithEvents Label4 As Label
    Friend WithEvents Label5 As Label
    Friend WithEvents Label6 As Label
    Friend WithEvents taxboxLabel As Label
    Friend WithEvents shipboxLabel As Label
    Friend WithEvents Label9 As Label
    Friend WithEvents cboMaterial As ComboBox
End Class
