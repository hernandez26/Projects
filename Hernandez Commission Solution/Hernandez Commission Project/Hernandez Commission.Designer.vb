<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()>
Partial Class HC
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()>
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
    <System.Diagnostics.DebuggerStepThrough()>
    Private Sub InitializeComponent()
        Me.EmployeeID = New System.Windows.Forms.TextBox()
        Me.Commission = New System.Windows.Forms.TextBox()
        Me.Calculate = New System.Windows.Forms.Button()
        Me.ebutton = New System.Windows.Forms.Button()
        Me.Label1 = New System.Windows.Forms.Label()
        Me.Label2 = New System.Windows.Forms.Label()
        Me.Label3 = New System.Windows.Forms.Label()
        Me.SuspendLayout()
        '
        'EmployeeID
        '
        Me.EmployeeID.Location = New System.Drawing.Point(61, 95)
        Me.EmployeeID.Name = "EmployeeID"
        Me.EmployeeID.Size = New System.Drawing.Size(100, 20)
        Me.EmployeeID.TabIndex = 0
        '
        'Commission
        '
        Me.Commission.Location = New System.Drawing.Point(194, 95)
        Me.Commission.Name = "Commission"
        Me.Commission.Size = New System.Drawing.Size(100, 20)
        Me.Commission.TabIndex = 1
        '
        'Calculate
        '
        Me.Calculate.Location = New System.Drawing.Point(86, 141)
        Me.Calculate.Name = "Calculate"
        Me.Calculate.Size = New System.Drawing.Size(75, 23)
        Me.Calculate.TabIndex = 2
        Me.Calculate.Text = "Calculate Commission"
        Me.Calculate.UseVisualStyleBackColor = True
        '
        'ebutton
        '
        Me.ebutton.Location = New System.Drawing.Point(194, 141)
        Me.ebutton.Name = "ebutton"
        Me.ebutton.Size = New System.Drawing.Size(75, 23)
        Me.ebutton.TabIndex = 3
        Me.ebutton.Text = "Exit"
        Me.ebutton.UseVisualStyleBackColor = True
        '
        'Label1
        '
        Me.Label1.AutoSize = True
        Me.Label1.Font = New System.Drawing.Font("Microsoft YaHei UI", 8.25!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label1.Location = New System.Drawing.Point(58, 79)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(79, 16)
        Me.Label1.TabIndex = 4
        Me.Label1.Text = "Employee ID:"
        '
        'Label2
        '
        Me.Label2.AutoSize = True
        Me.Label2.Font = New System.Drawing.Font("Microsoft YaHei UI", 8.25!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label2.Location = New System.Drawing.Point(191, 79)
        Me.Label2.Name = "Label2"
        Me.Label2.Size = New System.Drawing.Size(77, 16)
        Me.Label2.TabIndex = 5
        Me.Label2.Text = "Commission:"
        '
        'Label3
        '
        Me.Label3.AutoSize = True
        Me.Label3.Font = New System.Drawing.Font("Microsoft YaHei UI", 14.25!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label3.Location = New System.Drawing.Point(81, 33)
        Me.Label3.Name = "Label3"
        Me.Label3.Size = New System.Drawing.Size(232, 26)
        Me.Label3.TabIndex = 6
        Me.Label3.Text = "Commission Calculator"
        '
        'HC
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(358, 261)
        Me.Controls.Add(Me.Label3)
        Me.Controls.Add(Me.Label2)
        Me.Controls.Add(Me.Label1)
        Me.Controls.Add(Me.ebutton)
        Me.Controls.Add(Me.Calculate)
        Me.Controls.Add(Me.Commission)
        Me.Controls.Add(Me.EmployeeID)
        Me.Name = "HC"
        Me.Text = "Tech Company Comission Calculator"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub

    Friend WithEvents EmployeeID As TextBox
    Friend WithEvents Commission As TextBox
    Friend WithEvents Calculate As Button
    Friend WithEvents ebutton As Button
    Friend WithEvents Label1 As Label
    Friend WithEvents Label2 As Label
    Friend WithEvents Label3 As Label
End Class
