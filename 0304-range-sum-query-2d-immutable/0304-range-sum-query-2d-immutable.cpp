class NumMatrix {
public:

    vector<vector<int>> recMat;

    NumMatrix(vector<vector<int>>& matrix) {
        int rows = matrix.size();
        int cols = matrix[0].size();

        recMat = vector<vector<int>>(rows, vector<int>(cols));
        recMat[0][0] = matrix[0][0];

        for (int c = 1; c < cols; c++) {
            recMat[0][c] = recMat[0][c - 1] + matrix[0][c];
        }

        for (int r = 1; r < rows; r++) {
            recMat[r][0] = recMat[r - 1][0] + matrix[r][0];
        }

        for (int r = 1; r < rows; r++) {
            for (int c = 1; c < cols; c++) {
                recMat[r][c] = recMat[r - 1][c] + recMat[r][c - 1] - recMat[r - 1][c - 1] + matrix[r][c];
            }
        }

        // Print the calculated recMat
        cout << "Calculated RecMat:" << endl;
        for (const auto& row : recMat) {
            for (int val : row) {
                cout << val << " ";
            }
            cout << endl;
        }
    }


    int sumRegion(int row1, int col1, int row2, int col2) {
        if (row1 == 0 && col1 == 0) return recMat[row2][col2];
        else if (row1 == 0) return recMat[row2][col2] - recMat[row2][col1 - 1];
        else if (col1 == 0) return recMat[row2][col2] - recMat[row1 - 1][col2];
        else return  recMat[row2][col2] - recMat[row2][col1 - 1] - recMat[row1 - 1][col2] + recMat[row1 -1][col1 - 1];
    }
};