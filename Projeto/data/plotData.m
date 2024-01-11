clear all
close all
clc


%color for plots
dark_green = 1/255 * [0,100,0];
dark_blue = 1/255 * [3,37,126];
dark_red = 1/255 * [139, 0, 0];

version = "V2/";

%% Slots

% Sem Correção
filename = "slots_no_correction.csv";

if isfile(version + filename)
    df = readtable(version + filename);
    resultsSlots(df, "sem correção")
else
    fprintf("\n[Ficheiro não encontrado: %s\n", version + filename + "]")
end


% Sem Correção de Ofsset
filename = "slots_no_offset.csv";

if isfile(version + filename)
    df = readtable(version + filename);
    resultsSlots(df, "sem correção de Offset")
else
    fprintf("\n[Ficheiro não encontrado: %s\n", version + filename + "]")
end


% Com correção de Rate e Offset
filename = "slots_corrected.csv";

if isfile(version + filename)
    df = readtable(version + filename);
    resultsSlots(df, "com correção Rate e Offset")
else
    fprintf("\n[Ficheiro não encontrado: %s\n", version + filename + "]")
end

%% Clock A

% Sem correção
filename = "clockA_no_correction.csv";
if isfile(version + filename)
    df = readtable(version + filename);
    resultsClock(df, "Relógio A, sem correção")

else
    fprintf("\n[Ficheiro não encontrado: %s\n", version + filename + "]")
end

% Sem correção de offset
filename = "clockA_no_offset.csv";
if isfile(version + filename)
    df = readtable(version + filename);
    resultsClock(df, "Relógio A, sem correção de Offset")

else
    fprintf("\n[Ficheiro não encontrado: %s\n", version + filename + "]")
end


% Com correção de Rate e Offset
filename = "clockA_corrected.csv";
if isfile(version + filename)
    df = readtable(version + filename);
    resultsClock(df, "Relógio A, com correção de Rate e Offset")

else
    fprintf("\n[Ficheiro não encontrado: %s\n", version + filename + "]")
end

%% Clock B

% Sem correção
filename = "clockB_no_correction.csv";
if isfile(version + filename)
    df = readtable(version + filename);
    resultsClock(df, "Relógio B, sem correção")
else
    fprintf("\n[Ficheiro não encontrado: %s\n", version + filename + "]")
end

% Sem correção de Offset
filename = "clockB_no_offset.csv";
if isfile(version + filename)
    df = readtable(version + filename);
    resultsClock(df, "Relógio B, sem correção de Offset")
else
    fprintf("\n[Ficheiro não encontrado: %s\n", version + filename + "]")
end


% Com correção de Rate e Offset
filename = "clockB_corrected.csv";
if isfile(version + filename)
    df = readtable(version + filename);
    resultsClock(df, "Relógio B, com correção de Rate e Offset")
else
    fprintf("\n[Ficheiro não encontrado: %s\n", version + filename + "]")
end


function results = resultsSlots(df, header)
    dark_green = 1/255 * [0,100,0];
    dark_blue = 1/255 * [3,37,126];
    dark_red = 1/255 * [139, 0, 0];


    slots = calculate_diff(df);

    % Plot slots
    x = (1:length(slots)) .* 10 / 60;
    y = slots.*1000;
    ttl = 'Slots' + header;
    figure; plot(x, y, '-', 'color', dark_green); title(ttl); xlabel('Tempo (minutos)'); ylabel('Sincronização das slots (milissegundo)'); xlim([0 length(slots)*10/60]+1)

    fprintf("\nResultados da sincronização de slots " + header + ":\n" + ...
            "  - Diferença máxima:\t %f\n" + ...
            "  - Variação máxima: \t %f\n" + ...
            "  - Diferença média: \t %f\n", ...
            max(abs(slots)), max(slots)-min(slots), mean(slots))
end



function results = resultsClock(df, header)
    dark_green = 1/255 * [0,100,0];
    dark_blue = 1/255 * [3,37,126];
    dark_red = 1/255 * [139, 0, 0];

    x = (1:length(df.offset)) .* 5 / 60;
    figure;
    plot(x, df.offset, '-', 'color', dark_red); hold on;
    plot(x, df.rate - 1, '-', 'color', dark_green); hold on;
    plot(x, df.delay, '-', 'color', dark_blue); hold off 
    ttl = 'Parâmetros de Correção, ' + header;
    title(ttl); xlabel('Tempo (minutos)'); ylabel('Valor (milisegundos)'); legend('offset', 'rate', 'delay'); xlim([0 length(df.offset)*5/60]+1);

    fprintf("\nResultados dos parâmetros de correção, " + header + ":\n" + ...
            "  - Offset máximo:   \t %f\n" + ...
            "  - Diferença Offset:\t %f\n" + ...
            "  - Média Offset:    \t %f\n" + ...
            "  - Rate máximo:     \t %f\n" + ...
            "  - Diferença Rate:  \t %f\n" + ...
            "  - Média Offset:    \t %f\n" + ...
            "  - Delay máximo:    \t %f\n" + ...
            "  - Jitter:          \t %f\n" + ...
            "  - Média Delay:     \t %f\n", ...
            max(abs(df.offset)), max(df.offset)-min(df.offset), mean(df.offset), ...
            max(df.rate), max(df.rate)-min(df.rate), mean(df.rate), ...
            max(df.delay), max(df.delay)-min(df.delay), mean(df.delay))
end


function diff_data = calculate_diff(df_slots)
    slots = df_slots.slots;

    diff_data = diff(slots);
    diff_data = diff_data(diff_data < 5);
end