class TAD_LIF():
    def __init__(self, alpha=0.01, beta=0.95, max_threshold=5, min_threshold=0.002, fire_threshold=0.05, L_min=150,
                 L_max=300, Ts=3):
        super(TAD_LIF, self).__init__()
        self.mem = 0
        self.alpha = alpha
        self.beta = beta
        self.max_threshold = max_threshold
        self.min_threshold = min_threshold
        self.fire_threshold = fire_threshold
        self.L_min = L_min
        self.L_max = L_max
        self.Ts = Ts
        self.counter = 0
        self.buffer = []

    def LIF_update(self, input_data):
        """TAD-LIF Unit Update"""
        if sum(input_data) > self.Ts:
            X = sum([i * i * self.alpha for i in input_data])
        else:
            X = 0
        self.mem = min(self.beta * self.mem + X, self.max_threshold)  # update the membrane potential

    def ASD_process(self, input_data):
        """Process of Active Segment Detection"""
        self.LIF_update(list(input_data))
        if self.mem > self.fire_threshold:  # activate state
            self.counter = self.counter + 1
            self.buffer.append(input_data)
        else:  # inactivate state
            if self.mem < self.min_threshold:
                self.mem = 0
            if self.L_min < self.counter < self.L_max:
                return self.buffer
            else:
                self.counter = 0
                self.buffer = []
        return None
