' Name:         Payroll.vb
' Programmer:   Jonathan Hernandez 12/8/2017

Option Explicit On
Option Strict On
Option Infer Off

' base class
Public Class Bonus

    ' String property for SalesId and Double property for sales
    Public Property SalesId As String
    Public Property Sales As Double

    'Default constructor
    Public Sub New()
        _SalesId = String.Empty
        _Sales = 0
    End Sub

    'Parameterized constructor
    Public Sub New(ByVal strSID As String, ByVal dblSales As Double)
        SalesId = strSID
        Sales = dblSales
    End Sub

    'GetBonus method overridable
    Public Overridable Function GetBonus() As Double
        Return _Sales * 0.05
    End Function

End Class

' derived class
Public Class PremiumBonus
    'The inherits clause
    Inherits Bonus

    'Default constructor for derived class
    Public Sub New()
        MyBase.New()
    End Sub

    'Parameterized constructor for derived class
    Public Sub New(ByVal strID As String, ByVal dblSales As Double)
        MyBase.New(strID, dblSales)
    End Sub

    ' GetBonus method, overrides the one from base class
    Public Overrides Function GetBonus() As Double
        Return MyBase.GetBonus + (((MyBase.GetBonus / 0.05) - 2500) * 0.01)
    End Function

End Class
