% Convolution of Two Sequences

% Input sequences
x = input('Enter the first sequence x[n]: ');
h = input('Enter the second sequence h[n]: ');

% Built-in convolution
y_builtin = conv(x, h);

% Manual convolution
N1 = length(x);
N2 = length(h);
N = N1 + N2 - 1;
y_manual = zeros(1, N);

% Zero-padding
x_pad = [x, zeros(1, N2-1)];
h_pad = [h, zeros(1, N1-1)];

% Compute convolution manually
for n = 1:N
    for k = 1:n
        if (k <= N1) && ((n-k+1) <= N2)
            y_manual(n) = y_manual(n) + x(k) * h(n-k+1);
        end
    end
end

% Display results
disp('Convolution using built-in conv():');
disp(y_builtin);
disp('Convolution computed manually:');
disp(y_manual);