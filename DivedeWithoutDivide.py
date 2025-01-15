class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        divisorval =0;
        strnum = str(divisor);
        if str(divisor)[0] == "-":
            divisor = int(str(divisor)[1:]);
        if dividend == divisor:
            return 1;
        while True:
            if divisorval+divisorval< dividend:
                divisorval += divisor;
            else:
                break;
        if strnum[0] == "-":
            return  int(str("-" + str(divisorval)))//divisor;
        else:
            return divisorval//divisor;