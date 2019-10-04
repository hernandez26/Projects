Public Class Form1


    'This is the quanity text box
    Private Sub TextBox1_Enter(sender As Object, e As EventArgs) Handles TextBox1.Enter
        TextBox1.SelectAll()

    End Sub

    'This Permits only numerical entries into the Quanity textbox, as well as the backspace.
    Private Sub CancelKeys(sender As Object, e As KeyPressEventArgs) Handles TextBox1.KeyPress

        If (e.KeyChar < "0" OrElse e.KeyChar > "9") AndAlso
            e.KeyChar <> ControlChars.Back Then
            e.Handled = True
        End If
    End Sub

    'This allows The The Labels and Checkboxes to be cleared
    Private Sub ClearLabels(sender As Object, e As EventArgs) _
        Handles TextBox1.TextChanged, radFree.CheckedChanged, rad2.CheckedChanged, radNext.CheckedChanged

        subbox.Text = String.Empty
        taxbox.Text = String.Empty
        shipbox.Text = String.Empty
        Gtotalbox.Text = String.Empty

    End Sub

    'This fills the combo box 
    Private Sub frmMain_Load(sender As Object, e As EventArgs) Handles Me.Load
        cboMaterial.Items.Add("Plastic")
        cboMaterial.Items.Add("Metallic Plastic")
        cboMaterial.Items.Add("Stainless Steel")
        cboMaterial.SelectedIndex = 0
    End Sub

    'this displays the the sub total, tax, shipping charge, and grand total 
    Private Sub calcButton_Click(sender As Object, e As EventArgs) Handles calcButton.Click
        Dim pMRate As Double = 0.27
        Dim pCRate As Double = 1.5
        Dim mpMRate As Double = 0.57
        Dim mpCRate As Double = 1.5
        Dim stainlessRate As Double = 5.0
        Dim ssCRate As Double = 6.0
        Dim taxRate As Double = 0.1
        Dim sMaterial As String
        Dim dblVolume As Double
        Dim dblSub As Double
        Dim dblShip As Double
        Dim dblTax As Double
        Dim dbGrand As Double
        Dim shipStatus As String

        sMaterial =
        Convert.ToString(cboMaterial.SelectedItem.ToString)

        'This takes the number typed into Textbox1 and puts it into intNumT
        Integer.TryParse(TextBox1.Text, dblVolume)

        If radFree.Checked Then
            shipStatus = "F"
        ElseIf rad2.Checked Then
            shipStatus = "T"
        Else
            shipStatus = "N"
        End If

        'calculate sub total
        If sMaterial = "Plastic" Then
            dblSub = pCRate + (pMRate * dblVolume)
        ElseIf sMaterial = "Metallic Plastic" Then
            dblSub = mpCRate + (mpMRate * dblVolume)
        ElseIf sMaterial = "Stainless Steel" Then
            dblSub = ssCRate + (stainlessRate * dblVolume)
        End If

        ' calculate tax
        dblTax = dblSub * taxRate

        'calculate grand total
        dbGrand = dblSub + dblTax + dblShip

    End Sub

    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load

    End Sub

    Private Sub Label1_Click(sender As Object, e As EventArgs) Handles Label1.Click

    End Sub

    Private Sub ListBox1_SelectedIndexChanged(sender As Object, e As EventArgs)

    End Sub

End Class
