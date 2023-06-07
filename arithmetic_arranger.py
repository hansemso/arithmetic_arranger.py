import operator
from typing import Sequence, NamedTuple, Literal  #typing is a library containing these. From collections won't work.
#Tuple is just a list in ( ).  NamedTuple is key and value.

ops = {"+": operator.add, "-": operator.sub}


class Problem(NamedTuple):   #creates a subclass of tuples
    x: int   #
    y: int
    op: Literal['+', '-']

    @classmethod
    def parse(cls, s: str) -> 'Problem': #'' means look for a string named Problem. parse means look for a string named Problem and return
    #the NamedTuple in it.
        x, op, y = s.split()  #Now split the string in the tuple, i.e. x,y,op into pieces.

        for n in (x, y): #Now consider the integers in x and y above.
            if not n.isdigit():  #check if all characters are digits.
                raise ValueError('Error: Numbers must only contain digits.')  #Give warning if not.

        return cls(x=int(x), y=int(y), op=op)

    def validate(self) -> None:
        for n in (self.x, self.y):
            if abs(n) >= 1e4:
                raise ValueError('Error: Number cannot be more than four digits.')

        if self.op not in ops:
            raise ValueError(
                'Error: Operator must be '
                + ' or '.join(f"'{o}'" for o in ops.keys())
            )

    def format_lines(self, solve: bool = False) -> tuple[str, ...]:
        longest = max(self.x, self.y)  #max returns the highest number.
        width = len(str(longest))  #
        lines = (
            f'{self.x:>{width + 2}}',
            f'{self.op} {self.y:>{width}}',
            f'{"":->{width+2}}',
        )
        if solve:
            lines += (
                f'{self.answer:>{width+2}}',
            )
        return lines

    @property
    def answer(self) -> int:
        return ops[self.op](self.x, self.y)


def arithmetic_arranger(problem_strings: Sequence[str], solve: bool = False) -> None:  #Sequence is a class imported above. str is also a class.
#str() is a class function, converts numbers to string. Solve is a key, called below at last line.
    if len(problem_strings) > 5:
        print('Error: Too many problems.')
        return

    try:
        problems = [Problem.parse(s) for s in problem_strings]
        for problem in problems:
            problem.validate()
    except ValueError as e:
        print(e)
        return

    lines = zip(*(p.format_lines(solve) for p in problems))
    print(
        '\n'.join(
            '    '.join(groups) for groups in lines
        )
    )


if __name__ == "__main__":
    arithmetic_arranger((
        "32 + 698",
        "3801 - 2",
        "4 + 4553",
        "123 + 49",
        "1234 - 9876"
    ), solve=True)