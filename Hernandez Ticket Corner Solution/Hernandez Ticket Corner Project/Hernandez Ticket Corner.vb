' Name: Jonathan Hernandez
'Class: CIS-1510-Net01
' Assignment: Unit 3 Assignment: Project 1
'Date: 10/27/2017
Option Explicit On
Option Strict On
Option Infer Off

Public Class HernandezTicketCorner

    'This is the Clear button
    Private Sub Button2_Click(sender As Object, e As EventArgs) Handles clear.Click
        TextBox1.Text = ""

    End Sub

    'This is The main Title Label that reads " Ticket Corner"
    Private Sub Label1_Click(sender As Object, e As EventArgs) Handles Label1.Click

    End Sub

    'This the Form for the Hernandez Ticket Corner
    Private Sub HernandezTicketCorner_Load(sender As Object, e As EventArgs) Handles MyBase.Load

    End Sub

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
        Handles TextBox1.TextChanged, CheckBox1.CheckedChanged, CheckBox2.CheckedChanged, CheckBox3.CheckedChanged

        Label4.Text = String.Empty

    End Sub

    'This is the Calculate button
    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click

        'define the constant integers and variables
        Const intRegT As Integer = 35
        Const intVIPt As Integer = 85
        Const intAlbum As Integer = 20
        Const intVIPalbum As Integer = 5
        Const intTShirt As Integer = 25

        Dim intTprice As Integer
        Dim dblTotal As Integer
        Dim intNumT As Integer

        'This takes the number typed into Textbox1 and puts it into intNumT
        Integer.TryParse(TextBox1.Text, intNumT)


        'This is the algorithm used to determine ouput
        If CheckBox1.Checked And CheckBox2.Checked And CheckBox3.Checked Then
            intTprice = (intVIPt + intVIPalbum + intTShirt)
        ElseIf CheckBox2.Checked And CheckBox3.Checked Then
            intTprice = (intRegT + intAlbum + intTShirt)
        ElseIf CheckBox1.Checked And CheckBox2.Checked Then
            intTprice = (intVIPt + intVIPalbum)
        ElseIf CheckBox1.Checked And CheckBox3.Checked Then
            intTprice = (intVIPt + intTShirt)
        ElseIf CheckBox3.Checked Then
            intTprice = (intRegT + intTShirt)
        ElseIf CheckBox2.Checked Then
            intTprice = (intRegT + intAlbum)
        ElseIf CheckBox1.Checked Then
            intTprice = intVIPt
        Else
            intTprice = intRegT
        End If

        'This calculates the total
        dblTotal = (intNumT * intTprice)

        'This is the output ot label4. it displays the total
        Label4.Text = dblTotal.ToString("N2")

    End Sub

End Class
