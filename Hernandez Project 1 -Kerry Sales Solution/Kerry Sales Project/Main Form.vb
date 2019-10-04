' Name:         Kerry Sales Project
' Purpose:      Displays a salesperson's bonus
' Programmer:   Jonathan Hernandez 12/8/2017

Option Explicit On
Option Strict On
Option Infer Off

Public Class frmMain

    Private Sub btnExit_Click(sender As Object, e As EventArgs) Handles btnExit.Click
        Me.Close()
    End Sub

    Private Sub txtSales_Enter(sender As Object, e As EventArgs) Handles txtSales.Enter
        txtSales.SelectAll()
    End Sub

    Private Sub txtSales_KeyPress(sender As Object, e As KeyPressEventArgs) Handles txtSales.KeyPress
        If (e.KeyChar < "0" OrElse e.KeyChar > "9") AndAlso e.KeyChar <> "." AndAlso e.KeyChar <> ControlChars.Back Then
            e.Handled = True
        End If
    End Sub

    Private Sub txtSales_TextChanged(sender As Object, e As EventArgs) Handles txtSales.TextChanged
        lblBonus.Text = String.Empty
    End Sub

    Private Sub btnCalc_Click(sender As Object, e As EventArgs) Handles btnCalc.Click
        ' calculates and displays a bonus

        ' 2 doubles one to hold the typed Sales amount, and the other to hold the calculated bonus amount
        Dim SalesAmt As Double
        Dim BonusAmt As Double

        'reads sales amount entered int the sales the box
        Double.TryParse(txtSales.Text, SalesAmt)


        ' if the sales are over $2500, instantiate a PremiumBonus object
        ' and then calculate the bonus
        ' otherwise, instantiate a Bonus object and then calculate the bonus
        If SalesAmt > 2500 Then

            'PremiumBonus object Instantiated.
            Dim FinalBonus As New PremiumBonus(txtId.Text, SalesAmt)
            BonusAmt = FinalBonus.GetBonus

        Else

            'Bonus Object instantiated
            Dim FinalBonus As New Bonus(txtId.Text, SalesAmt)
            BonusAmt = FinalBonus.GetBonus

        End If



        ' display the bonus
        lblBonus.Text = BonusAmt.ToString("C2")

    End Sub
End Class
