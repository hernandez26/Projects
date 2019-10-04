'Name: Jonathan Hernandez
'Assignment: Unit 5 Project 2
'Class: CIS 1510-Net01
'Date: 12/29/2017
Option Explicit On
Option Strict On
Option Infer Off

Public Class HC
    'exit button to close program
    Private Sub ebutton_Click(sender As Object, e As EventArgs) Handles ebutton.Click
        Me.Close()

    End Sub

    Structure CommissionInfo
        Public EID As String
        Public Esales As String
    End Structure

    Private employeeInfo(10) As CommissionInfo
    'The calculate button that makes the program run.

    Private Sub Calculate_Click(sender As Object, e As EventArgs) Handles Calculate.Click


        Dim strEID As String
        Dim intSub As Integer
        Dim intCommish As Integer

        'reads number in ID text box
        strEID = EmployeeID.Text

        Do Until intSub = employeeInfo.Length OrElse
           strEID = employeeInfo(intSub).EID
            intSub += 1
        Loop
        'Displays commission
        If intSub < employeeInfo.Length Then
            employeeInfo(intSub).Esales.ToString()


            'Calculate and display total after discounts 
            intCommish = CInt(0.07 * CDbl(employeeInfo(intSub).Esales))
            Commission.Text = CType(intCommish, String)


        Else
            'Display error message in case invalid input is entered.
            MessageBox.Show("Information not found", "Error", MessageBoxButtons.OK, MessageBoxIcon.Information)

        End If

    End Sub

    Private Sub HC_Load(sender As Object, e As EventArgs) Handles Me.Load

        'declare a Streamreader variable
        Dim inFile As IO.StreamReader
        Dim strInfo As String
        Dim intInfo As String
        Dim i As Integer = 0


        If IO.File.Exists("sales.csv") Then
            'open the file input
            inFile = IO.File.OpenText("sales.csv")
            'process loop instructons until end of file
            Do Until inFile.Peek = -1
                strInfo = inFile.ReadLine
                intInfo = inFile.ReadLine
                employeeInfo(i).EID = strInfo
                employeeInfo(i).Esales = intInfo
                'lstdata.Items.Add(strInfo)


            Loop
            inFile.Close()
            'lstdata.SelectedIndex = 0

        Else
            MessageBox.Show("Cannot locate sales.csv", "Error Message", MessageBoxButtons.OK, MessageBoxIcon.Information)
        End If


    End Sub


End Class
