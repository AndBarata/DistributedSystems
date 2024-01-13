clear all
close all
clc

%% Header
%color for plots
dark_green = 1/255 * [0,100,0];
dark_blue = 1/255 * [3,37,126];
dark_red = 1/255 * [139, 0, 0];

% Versão indica o host utilizado_ 
%   - proto: Protótipos
%   - V1:    Primeiros teste com servidor pool.ntp.rg
%   - V2:    Testes com servidor pool.ntp.rg
%   - V3:    Testes com servidor ntp0.ntp-server.net
%   - V4:    Testes com o servidor a localhost

version = "V2/";

%% Slots

% Sem Correção
filename = "slots_no_correction.csv";

if isfile(version + filename)
    df = readtable(version + filename);
    resultsSlots(df, "sem correção", version)
    erroQuadratico(df, "sem correção", version)
else
    fprintf("\n[Ficheiro não encontrado: %s\n", version + filename + "]")
end


% Sem Correção de Ofsset
filename = "slots_no_offset.csv";

if isfile(version + filename)
    df = readtable(version + filename);
    resultsSlots(df, "sem correção de Offset", version)
else
    fprintf("\n[Ficheiro não encontrado: %s\n", version + filename + "]")
end


% Com correção de Rate e Offset
filename = "slots_corrected.csv";

if isfile(version + filename)
    df = readtable(version + filename);
    resultsSlots(df, "com correção Rate e Offset", version)
else
    fprintf("\n[Ficheiro não encontrado: %s\n", version + filename + "]")
end


% Com correção de Rate e Offset e delay,  T = 5
filename = "slots_corrected_delay.csv";

if isfile(version + filename)
    df = readtable(version + filename);
    resultsSlots(df, "com correção Rate e Offset considerando delay, T = 5 ", version)
    erroQuadratico(df, "com correção Rate e Offset considerando delay, T = 5 ", version)

else
    fprintf("\n[Ficheiro não encontrado: %s\n", version + filename + "]")
end


% Com correção de Rate e Offset, T = 2
filename = "slots_corrected_2NTP.csv";

if isfile(version + filename)
    df = readtable(version + filename);
    resultsSlots(df, "com correção Rate e Offset T = 2", version)
else
    fprintf("\n[Ficheiro não encontrado: %s\n", version + filename + "]")
end


% Com correção de Rate e Offset e delay, T = 2
filename = "slots_corrected_delay_2NTP.csv";

if isfile(version + filename)
    df = readtable(version + filename);
    resultsSlots(df, "com correção Rate e Offset considerando delay, T = 2", version)
else
    fprintf("\n[Ficheiro não encontrado: %s\n", version + filename + "]")
end


% Com correção de Rate e Offset, T = 15
filename = "slots_corrected_15NTP.csv";

if isfile(version + filename)
    df = readtable(version + filename);
    resultsSlots(df, "com correção Rate e Offset T = 15", version)
else
    fprintf("\n[Ficheiro não encontrado: %s\n", version + filename + "]")
end


% Com correção de Rate e Offset e delay, T = 15
filename = "slots_corrected_delay_15NTP.csv";

if isfile(version + filename)
    df = readtable(version + filename);
    resultsSlots(df, "com correção Rate e Offset considerando delay, T = 15", version)
else
    fprintf("\n[Ficheiro não encontrado: %s\n", version + filename + "]")
end





%% Clock A

% Sem correção
filename = "clockA_corrected_delay.csv";
if isfile(version + filename)
    df = readtable(version + filename);
    resultsClock(df, "Relógio A, sem correção", version)

else
    fprintf("\n[Ficheiro não encontrado: %s\n", version + filename + "]")
end

% Sem correção de offset
filename = "clockA_no_offset.csv";
if isfile(version + filename)
    df = readtable(version + filename);
    resultsClock(df, "Relógio A, sem correção de Offset", version)

else
    fprintf("\n[Ficheiro não encontrado: %s\n", version + filename + "]")
end


% Com correção de Rate e Offset
filename = "clockA_corrected.csv";
if isfile(version + filename)
    df = readtable(version + filename);
    resultsClock(df, "Relógio A, com correção de Rate e Offset", version)

else
    fprintf("\n[Ficheiro não encontrado: %s\n", version + filename + "]")
end

% Com correção de Rate e Offset considerando delay 
filename = "clockA_corrected_delay.csv";
if isfile(version + filename)
    df = readtable(version + filename);
    resultsClock(df, "Relógio A, com correção de Rate e Offset considerando delay ", version)

else
    fprintf("\n[Ficheiro não encontrado: %s\n", version + filename + "]")
end


% Com correção de Rate e Offset, T = 2
filename = "clockA_corrected_2NTP.csv";
if isfile(version + filename)
    df = readtable(version + filename);
    resultsClock(df, "Relógio A, com correção de Rate e Offset, T = 2 ", version)

else
    fprintf("\n[Ficheiro não encontrado: %s\n", version + filename + "]")
end


% Com correção de Rate e Offset considerando delay, T = 2
filename = "clockA_corrected_delay_2NTP.csv";
if isfile(version + filename)
    df = readtable(version + filename);
    resultsClock(df, "Relógio A, com correção de Rate e Offset considerando delay, T = 2 ", version)

else
    fprintf("\n[Ficheiro não encontrado: %s\n", version + filename + "]")
end


% Com correção de Rate e Offset, T = 15
filename = "clockA_corrected_15NTP.csv";
if isfile(version + filename)
    df = readtable(version + filename);
    resultsClock(df, "Relógio A, com correção de Rate e Offset, T = 15 ", version)

else
    fprintf("\n[Ficheiro não encontrado: %s\n", version + filename + "]")
end


% Com correção de Rate e Offset considerando delay, T = 15
filename = "clockA_corrected_delay_15NTP.csv";
if isfile(version + filename)
    df = readtable(version + filename);
    resultsClock(df, "Relógio A, com correção de Rate e Offset considerando delay, T = 15 ", version)

else
    fprintf("\n[Ficheiro não encontrado: %s\n", version + filename + "]")
end



%% Clock B

% Sem correção
filename = "clockB_no_correction.csv";
if isfile(version + filename)
    df = readtable(version + filename);
    resultsClock(df, "Relógio B, sem correção", version)
else
    fprintf("\n[Ficheiro não encontrado: %s\n", version + filename + "]")
end

% Sem correção de Offset
filename = "clockB_no_offset.csv";
if isfile(version + filename)
    df = readtable(version + filename);
    resultsClock(df, "Relógio B, sem correção de Offset", version)
else
    fprintf("\n[Ficheiro não encontrado: %s\n", version + filename + "]")
end


% Com correção de Rate e Offset
filename = "clockB_corrected.csv";
if isfile(version + filename)
    df = readtable(version + filename);
    resultsClock(df, "Relógio B, com correção de Rate e Offset", version)
else
    fprintf("\n[Ficheiro não encontrado: %s\n", version + filename + "]")
end


% Com correção de Rate e Offset considerando delay, T = 5
filename = "clockB_corrected_delay.csv";
if isfile(version + filename)
    df = readtable(version + filename);
    resultsClock(df, "Relógio B, com correção de Rate e Offset considerando delay, T = 5 ", version)

else
    fprintf("\n[Ficheiro não encontrado: %s\n", version + filename + "]")
end


% Com correção de Rate e Offset, T = 2
filename = "clockB_corrected_2NTP.csv";
if isfile(version + filename)
    df = readtable(version + filename);
    resultsClock(df, "Relógio B, com correção de Rate e Offset, T = 2 ", version)

else
    fprintf("\n[Ficheiro não encontrado: %s\n", version + filename + "]")
end



% Com correção de Rate e Offset considerando delay, T = 2
filename = "clockB_corrected_delay_2NTP.csv";
if isfile(version + filename)
    df = readtable(version + filename);
    resultsClock(df, "Relógio B, com correção de Rate e Offset considerando delay, T = 2 ", version)

else
    fprintf("\n[Ficheiro não encontrado: %s\n", version + filename + "]")
end


% Com correção de Rate e Offset, T = 15
filename = "clockB_corrected_15NTP.csv";
if isfile(version + filename)
    df = readtable(version + filename);
    resultsClock(df, "Relógio B, com correção de Rate e Offset, T = 15 ", version)

else
    fprintf("\n[Ficheiro não encontrado: %s\n", version + filename + "]")
end


% Com correção de Rate e Offset considerando delay, T = 15
filename = "clockB_corrected_delay_15NTP.csv";
if isfile(version + filename)
    df = readtable(version + filename);
    resultsClock(df, "Relógio B, com correção de Rate e Offset considerando delay, T = 15 ", version)

else
    fprintf("\n[Ficheiro não encontrado: %s\n", version + filename + "]")
end




function erro = erroQuadratico(df, header, version)
    dark_green = 1/255 * [0,100,0];
    dark_blue = 1/255 * [3,37,126];
    dark_red = 1/255 * [139, 0, 0];

    slots = calculate_diff(df).^2;
    %slots = slots(slots < 100*mean(slots));

    % Plot slots
    x = (1:length(slots)) .* 10 / 60;
    y = slots.*1000;
    ttl = 'Slots erro quadrático ' + header;
    figure; plot(x, y, '-', 'color', dark_red); title(ttl); xlabel('Tempo (minutos)'); ylabel('Erro quadrático'); xlim([0 length(slots)*10/60]+1)
   
end


function results = resultsSlots(df, header, version)
    dark_green = 1/255 * [0,100,0];
    dark_blue = 1/255 * [3,37,126];
    dark_red = 1/255 * [139, 0, 0];


    slots = calculate_diff(df);

    % Plot slots
    x = (1:length(slots)) .* 10 / 60;
    y = slots.*1000;
    ttl = 'Slots ' + header;
    figure; plot(x, y, '-', 'color', dark_green); title(ttl); xlabel('Tempo (minutos)'); ylabel('Sincronização das slots (milissegundo)'); xlim([0 length(slots)*10/60]+1)

    % Guardar figura
    %saveas(gcf, 'Resultados/' + version + "Slots " + header + ".png")
    %saveas(gcf, 'Resultados/' + version + "Slots " + header + ".fig")
    fprintf("\nResultados da sincronização de slots " + header + ":\n" + ...
        "  - Diferença máxima:\t %.4f\n" + ...
        "  - Variação máxima: \t %.4f\n" + ...
        "  - Diferença média: \t %.4f\n", ...
        max(abs(slots)), max(slots)-min(slots), mean(slots))
   
end



function results = resultsClock(df, header, version)
    dark_green = 1/255 * [0,100,0];
    dark_blue = 1/255 * [3,37,126];
    dark_red = 1/255 * [139, 0, 0];

    x = (1:length(df.offset)) .* 5 / 60;

    % Plot offset, rate and delay
    figure;
    plot(x, df.offset, '-', 'color', dark_red); hold on;
    plot(x, df.rate - 1, '-', 'color', dark_green); hold on;
    plot(x, df.delay, '-', 'color', dark_blue); hold off
    ttl = 'Parâmetros de Correção, ' + header;
    title(ttl); xlabel('Tempo (minutos)'); ylabel('Valor (milisegundos)'); legend('offset', 'rate', 'delay'); xlim([0 length(df.offset)*5/60]+1);
    % Guardar figura
    %saveas(gcf, 'Resultados/' + version + "Parâmetros de Correção " + header + ".png")
    %saveas(gcf, 'Resultados/' + version + "Parâmetros de Correção " + header + ".fig")

    fprintf("\nResultados dos parâmetros de correção, " + header + ":\n" + ...
        "  - Offset máximo:   \t %.4f\n" + ...
        "  - Diferença Offset:\t %.4f\n" + ...
        "  - Média Offset:    \t %.4f\n" + ...
        "  - Rate máximo:     \t %.4f\n" + ...
        "  - Diferença Rate:  \t %.4f\n" + ...
        "  - Média Rate:    \t %.4f\n" + ...
        "  - Delay máximo:    \t %.4f\n" + ...
        "  - Jitter:          \t %.4f\n" + ...
        "  - Média Delay:     \t %.4f\n", ...
        max(abs(df.offset)), max(df.offset)-min(df.offset), mean(df.offset), ...
        max(df.rate), max(df.rate)-min(df.rate), mean(df.rate), ...
        max(df.delay), max(df.delay)-min(df.delay), mean(df.delay))
end


function diff_data = calculate_diff(df_slots)
    slots = df_slots.slots;
    diff_data = [];

    for i = 1:2:length(slots)
        if i+1 > length(slots)
            break
        end
        diff = abs(slots(i+1) - slots(i));
        diff_data = [diff_data, diff];
        %if diff > 5, fprintf("\n%d - %f | %f\n", i, slots(i), slots(i+1)); return; end
    end

end