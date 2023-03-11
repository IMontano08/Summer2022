#include <iostream>
using namespace std;
main()
{
    string Answer;
    bool setLoop = false;
    while (setLoop == false)
    {
        cout << "Would you like a green, red, or blue car? Please put all answers in lowercase only." << endl;
        cin >> Answer;
        
        if (Answer == "red")
            {
                cout << "You chose a red car" << endl;
                setLoop = true;
            }
        else if (Answer == "blue")
            {
                cout << "You chose a blue car" << endl;
                setLoop = true;
            }
        else if (Answer == "green")
            {
                cout << "You chose a green car" << endl;
                setLoop = true;
            }
        else
            cout << "Please select a valid option or make sure that your answer is in all lowercase" << endl;
    }
}