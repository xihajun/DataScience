fname= '\\ads.bris.ac.uk\filestore\myfiles\StudentPG1\username\Downloads\honeypot.json\honeypot.json'
fid = fopen(fname);
tline = fgetl(fid);
i=1;
j=1;
while ischar(tline)
    temp{i}=matlab.internal.webservices.fromJSON(tline);
    i=i+1;
    if fix(i/10000/j)>0
       j=j+1
    end
    tline = fgetl(fid);
   
end
fclose(fid);
