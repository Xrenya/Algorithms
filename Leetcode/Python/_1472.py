class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current_tab = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.current_tab + 1]
        self.history.append(url)
        self.current_tab += 1
        

    def back(self, steps: int) -> str:
        current_tab = self.current_tab - steps
        self.current_tab = max(0, current_tab)
        return self.history[max(0, current_tab)]

    def forward(self, steps: int) -> str:
        current_tab = self.current_tab + steps
        self.current_tab = min(len(self.history) - 1, current_tab)
        return self.history[min(len(self.history) - 1, current_tab)]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
