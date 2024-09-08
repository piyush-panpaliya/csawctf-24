extern struct_0 *g_403fd8;

long long _init()
{
    struct struct_0 **v1;  // rax, Other Possible Types: unsigned long

    v1 = g_403fd8;
    if (g_403fd8)
        v1 = g_403fd8();
    return v1;
}

extern unsigned long long g_403ff0;

long long sub_401020()
{
    unsigned long v0;  // [bp-0x8]

    v0 = g_403ff0;
    goto *((long long *)4210680);
}

long long _start()
{
    char v0;  // [bp+0x0], Other Possible Types: unsigned long
    unsigned long v1;  // [bp+0x8]
    unsigned long long v2;  // rsi
    unsigned long v3;  // rax
    unsigned long long v4;  // rdx

    v2 = *((long long *)&v0);
    v0 = v3;
    __libc_start_main(main, v2, &v1, 0, 0, v4); /* do not return */
}

// No decompilation output for function sub_401175

// No decompilation output for function sub_401176

extern char __TMC_END__;
extern unsigned long long g_403fd0;

void sub_401180()
{
    return;
}

extern unsigned long long g_403fe0;

long long sub_4011a9()
{
    return 0;
}

extern unsigned long long __dso_handle;
extern struct_0 *g_403fb8;
extern char g_4042f8;

long long sub_4011f0()
{
    unsigned long v0;  // [bp-0x8]
    char v1;  // [bp+0x0]
    unsigned long v3;  // rax

    if (g_4042f8)
        return v3;
    v0 = &v1;
    if (!g_403fb8)
    {
        g_4042f8 = 1;
        v3 = (unsigned long long)sub_401180();
        return v3;
    }
    g_403fb8(__dso_handle);
}

long long sub_401240()
{
}

typedef struct struct_0 {
    char field_0;
} struct_0;

extern char _ZSt3cin@GLIBCXX_3.4;
extern char __bss_start;
extern char buf;

int main()
{
    char v0;  // [bp-0x295]
    unsigned int v1;  // [bp-0x294]
    unsigned int v2;  // [bp-0x290]
    unsigned int v3;  // [bp-0x28c]
    unsigned long v4;  // [bp-0x288]
    char v5;  // [bp-0x280], Other Possible Types: unsigned long
    struct_0 *v6;  // [bp-0x278]
    struct_0 *v7;  // [bp-0x270]
    char v8;  // [bp-0x268]
    char v9;  // [bp-0x248]
    char v10;  // [bp-0x31]
    unsigned long v11;  // [bp-0x30]
    unsigned long long *v13;  // fs

    v11 = v13[5];
    std::__cxx11::basic_string::__ctor__(&v8);
    std::basic_ostream& std::operator<<(&__bss_start, "Tell me what you know about *nix philosophies: ");
    std::basic_istream& std::operator>>(&_ZSt3cin@GLIBCXX_3.4, &v8);
    v1 = 0;
    for (v2 = 1; v2 < (unsigned long long)std::__cxx11::basic_string::size const(); v2 += 1)
    {
        v10 = *((char *)(unsigned long long)std::__cxx11::basic_string::operator[](&v8));
        v7 = &v5;
        std::__cxx11::basic_string::__ctor__(&v9, &v10);
        std::__new_allocator::__base_dtor__(&v5);
        v6 = &v9;
        v4 = (unsigned long long)std::__cxx11::basic_string::begin(v6);
        v5 = (unsigned long long)std::__cxx11::basic_string::end(v6);
        while ((char)bool __gnu_cxx::operator!=(&v4, &v5))
        {
            v0 = *((char *)__gnu_cxx::__normal_iterator::operator* const(&v4));
            v1 += v0;
            __gnu_cxx::__normal_iterator::operator++(&v4);
        }
        std::__cxx11::basic_string::__dtor__(&v9);
    }
    v3 = read(v1 - 1603, &buf, 32);
    if (strcmp("make every program a filter\n", &buf))
    {
        std::basic_ostream& std::operator<<(&__bss_start, "You still lack knowledge about *nix sorry");
        std::ostream::operator<<();
    }
    else
    {
        std::basic_ifstream::__ctor__(&v9, "flag.txt");
        if (!(char)std::basic_ios::good const())
        {
            std::basic_ostream& std::operator<<((unsigned long long)std::ostream::operator<<(), "flag.txt: No such file or directory");
            std::ostream::operator<<();
            std::basic_ostream& std::operator<<(&__bss_start, "If you're running this locally, then running it on the remote server should give you the flag!");
            std::ostream::operator<<();
        }
        else
        {
            std::basic_ostream& std::operator<<((unsigned long long)std::ostream::operator<<(), "Welcome to pwning ^_^");
            std::ostream::operator<<();
            system("/bin/cat flag.txt");
        }
        std::basic_ifstream::__dtor__(&v9);
    }
    std::__cxx11::basic_string::__dtor__(&v8);
    if (v11 != v13[5])
        __stack_chk_fail(); /* do not return */
    return 0;
}

int sub_401599()
{
    unsigned long v1;  // [bp+0xfffe0]
    unsigned long long *v2;  // fs

    std::__new_allocator::__base_dtor__(rbp<8> - 632);
    std::__cxx11::basic_string::__dtor__(rbp<8> - 608);
    if (v1 != v2[5])
        __stack_chk_fail(); /* do not return */
    _Unwind_Resume(); /* do not return */
}

long long sub_4015ae()
{
    std::basic_ifstream::__dtor__(rbp<8> - 576);
}

long long sub_4015c2()
{
}

int bool __gnu_cxx::operator!=(unsigned long long a0, unsigned long long a1)
{
    unsigned long v0;  // [bp-0x10]
    unsigned long v2;  // rbx
    unsigned long long v4;  // rax
    unsigned long long v5;  // rbx

    v0 = v2;
    v4 = *((long long *)__gnu_cxx::__normal_iterator::base const(a1));
    *((char *)&v4) = *((long long *)__gnu_cxx::__normal_iterator::base const(a0)) != v4;
    v5 = v0;
    return v4;
}

void __gnu_cxx::__normal_iterator::operator++(unsigned long long *a0)
{
    char v0;  // [bp-0x8]
    unsigned long long v2;  // rbp

    *(a0) = *(a0) + 1;
    v2 = *((long long *)&v0);
    return;
}

int __gnu_cxx::__normal_iterator::operator* const(unsigned long long *a0)
{
    return *(a0);
}

void std::__new_allocator::__base_dtor__(unsigned long a0)
{
    unsigned long v0;  // [bp-0x10]
    char v1;  // [bp-0x8]
    unsigned long long v3;  // rbp

    v0 = a0;
    v3 = *((long long *)&v1);
    return;
}

int __gnu_cxx::__normal_iterator::base const(unsigned long a0)
{
    return a0;
}

long long _fini()
{
    unsigned long v1;  // rax

    return v1;
}



// ddddddddddddddddg csawctf{-3v3ry7h1ng_15_4_f1l3}
