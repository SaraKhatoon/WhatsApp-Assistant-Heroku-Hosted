def syllabus_f2(subject):
    
    print(subject)
    if subject.find('ss')!=-1:
        sub="""Module-1Introduction to System Software \n Introduction to System Software, Machine Architecture of SIC and SIC/XE.\n
            Assemblers: Basic assembler functions, machine dependent assembler features, machine independent assembler features, assembler design options \n
            Macroprocessors: Basicmacro processor functions\n
            Module-2Loaders and Linkers\n 
            Loaders and Linkers:\n
            Basic Loader Functions, Machine Dependent Loader Features, Machine Independent Loader Features, Loader Design Options, Implementation Examples.\n
            Module-3 Introduction \n
            Introduction:
            Language Processors, The structure of a compiler, The evaluation of programming languages, The science of building compiler, Applications of compiler technology, Programming language basics \n
            Lexical Analysis:\n
            The role of lexical analyzer, Input buffering, Specifications of token, recognition of tokens, lexical analyzer generator, Finite automate.\n
            Module-4 Syntax Analysis \n
            Syntax Analysis:
            Introduction, Role Of Parsers, Context Free Grammars, Writing a grammar, Top Down Parsers, Bottom-Up Parsers, Operator-Precedence Parsing \n
            Module-5 Syntax Directed Translation \n
            Syntax Directed Translation, Intermediate code generation, Code generation"""
    elif subject.find('os')!=-1:
        sub="""Module-1 Introduction  \n
            Introduction - Cyber Attacks, Defence Strategies and Techniques, Guiding Principles, Mathematical Background for Cryptography - Modulo Arithmetic’s, The Greatest Comma Divisor, Useful Algebraic Structures, Chinese Remainder Theorem, Basics of Cryptography - Preliminaries, Elementary Substitution Ciphers, Elementary Transport Ciphers, Other Cipher Properties, Secret Key Cryptography – Product Ciphers, DES Construction. \n
            Module-2 Public Key Cryptography and RSA \n
            Public Key Cryptography and RSA – RSA Operations, Why Does RSA Work?, Performance, Applications, Practical Issues, Public Key Cryptography Standard (PKCS), Cryptographic Hash - Introduction, Properties, Construction, Applications and Performance, The Birthday Attack, Discrete Logarithm and its Applications - Introduction, Diffie-Hellman Key Exchange, Other Applications. \n
            Module-3 Key Management \n
            Key Management - Introduction, Digital Certificates, Public Key Infrastructure, Identity–based Encryption, Authentication–I - One way Authentication, Mutual Authentication, Dictionary Attacks, Authentication – II – Centalised Authentication, The Needham-Schroeder Protocol, Kerberos, Biometrics, IPSec- Security at the Network Layer – Security at Different layers: Pros and Cons, IPSec in Action, Internet Key Exchange (IKE) Protocol, Security Policy and IPSEC, Virtual Private Networks, Security at the Transport Layer - Introduction, SSL Handshake Protocol, SSL Record Layer Protocol, OpenSSL. \n
            Module-4 IEEE 802.11 Wireless LAN Security \n
            IEEE 802.11 Wireless LAN Security - Background, Authentication, Confidentiality and Integrity, Viruses, Worms, and Other Malware, Firewalls – Basics, Practical Issues, Intrusion Prevention and Detection - Introduction, Prevention Versus Detection, Types of Instruction Detection Systems, DDoS Attacks Prevention/Detection, Web Service Security – Motivation, Technologies for Web Services, WS- Security, SAML, Other Standards. \n
            Module-5 IT act aim and objectives \n
            IT act aim and objectives, Scope of the act, Major Concepts, Important provisions, Attribution, acknowledgement, and dispatch of electronic records, Secure electronic records and secure digital signatures, Regulation of certifying authorities: Appointment of Controller and Other officers, Digital Signature certificates, Duties of Subscribers, Penalties and adjudication, The cyber regulations appellate tribunal, Offences, Network service providers not to be liable in certain cases, Miscellaneous Provisions. \n"""
    elif subject.find('cg')!=-1:
        sub="""Module-1 Overview: Computer Graphics and OpenGL \n
              Overview: Computer Graphics and OpenGL:
              Computer Graphics:Basics of computer graphics, Application of Computer Graphics, Video Display Devices: Random Scan and Raster Scan displays, color CRT monitors, Flat panel displays. Raster-scan systems: video controller, raster scan Display processor, graphics workstations and viewing systems, Input devices, graphics networks, graphics on the internet, graphics software. OpenGL: Introduction to OpenGL ,coordinate reference frames, specifying two-dimensional world coordinate reference frames in OpenGL, OpenGL point functions, OpenGL line functions, point attributes, line attributes, curve attributes, OpenGL point attribute functions, OpenGL line attribute functions, Line drawing algorithms(DDA, Bresenham’s), circle generation algorithms(Bresenham’s). \n
              Module-2 Fill area Primitives, 2D Geometric Transformations and 2D viewing \n
              Fill area Primitives, 2D Geometric Transformations and 2D viewing:
              Fill area Primitives: Polygon fill-areas, OpenGL polygon fill area functions, fill area attributes, general scan line polygon fill algorithm, OpenGL fill-area attribute functions. 2DGeometric Transformations: Basic 2D Geometric Transformations, matrix representations and homogeneous coordinates. Inverse transformations, 2DComposite transformations, other 2D transformations, raster methods for geometric transformations, OpenGL raster transformations, OpenGL geometric transformations function, 2D viewing: 2D viewing pipeline, OpenGL 2D viewing functions. \n
              Module-3 Clipping,3D Geometric Transformations, Color and Illumination Models \n
              Clipping,3D Geometric Transformations, Color and Illumination Models:
              Clipping: clipping window, normalization and viewport transformations, clipping algorithms,2D point clipping, 2D line clipping algorithms: cohen-sutherland line clipping only -polygon fill area clipping: Sutherland-Hodgeman polygon clipping algorithm only.3DGeometric Transformations: 3D translation, rotation, scaling, composite 3D transformations, other 3D transformations, affine transformations, OpenGL geometric transformations functions. Color Models: Properties of light, color models, RGB and CMY color models. Illumination Models: Light sources, basic illumination models-Ambient light, diffuse reflection, specular and phong model, Corresponding openGL functions. \n
              Module-4 3D Viewing and Visible Surface Detection \n
              3D Viewing and Visible Surface Detection:
              3DViewing:3D viewing concepts, 3D viewing pipeline, 3D viewing coordinate parameters , Transformation fromworld to viewing coordinates, Projection transformation, orthogonal projections, perspective projections, The viewport transformation and 3D screen coordinates. OpenGL 3D viewing functions. Visible Surface Detection Methods: Classification of visible surface Detection algorithms, back face detection, depth buffer method and OpenGL visibility detection functions. \n
              Module-5 Input& interaction, Curves and Computer Animation \n
              Input& interaction, Curves and Computer Animation:
              Input and Interaction: Input devices, clients and servers, Display Lists, Display Lists and Modelling, Programming Event Driven Input, Menus Picking, Building Interactive Models, Animating Interactive programs, Design of Interactive programs, Logic operations .Curved surfaces, quadric surfaces, OpenGL Quadric-Surface and Cubic-Surface Functions, Bezier Spline Curves, Bezier surfaces, OpenGL curve functions. Corresponding openGL functions. \n"""
    elif subject.find('py')!=-1:
        sub="""Module – 1 
                Why should you learn to write programs, Variables, expressions and statements, Conditional execution, Functions
                Module – 2
                Iteration, Strings, Files 
                Module – 3
                Lists, Dictionaries, Tuples, Regular Expressions 
                Module – 4
                Classes and objects, Classes and functions, Classes and methods
                Module – 5
                Networked programs, Using Web Services, Using databases and SQL """
    elif subject.find('cns')!=-1:
        sub="""Module – 1 
                Introduction - Cyber Attacks, Defence Strategies and Techniques, Guiding Principles, Mathematical Background for Cryptography - Modulo Arithmetic’s,
                The Greatest Comma Divisor, Useful Algebraic Structures, Chinese Remainder
                Theorem, Basics of Cryptography - Preliminaries, Elementary Substitution
                Ciphers, Elementary Transport Ciphers, Other Cipher Properties, Secret Key
                Cryptography – Product Ciphers, DES Construction.

                Module – 2
                Public Key Cryptography and RSA – RSA Operations, Why Does RSA Work?,
                Performance, Applications, Practical Issues, Public Key Cryptography Standard
                (PKCS), Cryptographic Hash - Introduction, Properties, Construction,
                Applications and Performance, The Birthday Attack, Discrete Logarithm and its
                Applications - Introduction, Diffie-Hellman Key Exchange, Other Applications.

                Module – 3
                Key Management - Introduction, Digital Certificates, Public Key Infrastructure,
                Identity–based Encryption, Authentication–I - One way Authentication, Mutual
                Authentication, Dictionary Attacks, Authentication – II – Centalised
                Authentication, The Needham-Schroeder Protocol, Kerberos, Biometrics, IPSecSecurity at the Network Layer – Security at Different layers: Pros and Cons,
                IPSec in Action, Internet Key Exchange (IKE) Protocol, Security Policy and
                IPSEC, Virtual Private Networks, Security at the Transport Layer - Introduction,
                SSL Handshake Protocol, SSL Record Layer Protocol, OpenSSL.

                Module – 4
                IEEE 802.11 Wireless LAN Security - Background, Authentication,
                Confidentiality and Integrity, Viruses, Worms, and Other Malware, Firewalls –
                Basics, Practical Issues, Intrusion Prevention and Detection - Introduction,
                Prevention Versus Detection, Types of Instruction Detection Systems, DDoS
                Attacks Prevention/Detection, Web Service Security – Motivation, Technologies
                for Web Services, WS- Security, SAML, Other Standards.

                Module – 5
                IT act aim and objectives, Scope of the act, Major Concepts, Important
                provisions, Attribution, acknowledgement, and dispatch of electronic records,
                Secure electronic records and secure digital signatures, Regulation of certifying
                authorities: Appointment of Controller and Other officers, Digital Signature
                certificates, Duties of Subscribers, Penalties and adjudication, The cyber
                regulations appellate tribunal, Offences, Network service providers not to be
                liable in certain cases, Miscellaneous Provisions"""
    elif subject.find('or')!=-1:
        sub="""Module – 1 
                Introduction, Linear Programming: Introduction: The origin, natureand impact
                of OR; Defining the problem and gathering data; Formulating amathematical
                model; Deriving solutions from the model; Testing the model;Preparing to apply
                the model; Implementation .
                Introduction to Linear Programming Problem (LPP): Prototype example,
                Assumptions of LPP, Formulation of LPP and Graphical method various
                examples.
                
                Module – 2
                Simplex Method – 1: The essence of the simplex method; Setting up the simplex
                method; Types of variables, Algebraof the simplex method; the simplex method
                in tabular form; Tie breaking inthe simplex method, Big M method, Two phase
                method.
               
                Module – 3
                Simplex Method – 2: Duality Theory - The essence of duality theory,
                Primaldual relationship, conversion of primal to dual problem and vice versa.
                The dual simplex method.
                
                Module – 4
                Transportation and Assignment Problems: The transportation problem, Initial
                Basic Feasible Solution (IBFS) by North West Corner Rule method, Matrix
                Minima Method, Vogel’s Approximation Method. Optimal solution by Modified
                Distribution Method (MODI). The Assignment problem; A Hungarian algorithm
                for the assignment problem. Minimization and Maximization varieties in
                transportation and assignment problems.
                
                Module – 5
                Game Theory: Game Theory: The formulation of twopersons, zero sum games;
                saddle point, maximin and minimax principle, Solving simple games- a prototype
                example;Games with mixed strategies; Graphical solution procedure.
                Metaheuristics: The nature of Metaheuristics, Tabu Search,
                SimulatedAnnealing, Genetic Algorithms. """

    print(sub)
    return sub
    

def syllabus_m(subject,module):
    modwise=''
    syb={"ss":{'1':""" Module-1 Introduction to System Software, Introduction to System Software, Machine Architecture of SIC n SIC/XE. Assemblers: Basic assembler functions, machine dependent assembler features, machine independent assembler features, assembler design options 
        Macroprocessors: Basicmacro processor functions""",'2':"""Module 2 :Fill area Primitives, 2D Geometric Transformations and 2D viewing \n
        Fill area Primitives, 2D Geometric Transformations and 2D viewing:
        Fill area Primitives: Polygon fill-areas, OpenGL polygon fill area functions, fill area attributes, general scan line polygon fill algorithm, OpenGL fill-area attribute functions. 2DGeometric Transformations: Basic 2D Geometric Transformations, matrix representations and homogeneous coordinates. Inverse transformations, 2DComposite transformations, other 2D transformations, raster methods for geometric transformations, OpenGL raster transformations, OpenGL geometric transformations function, 2D viewing: 2D viewing pipeline, OpenGL 2D viewing functions. """,'3':""" Module 3 :Introduction:
        Language Processors, The structure of a compiler, The evaluation of programming languages, The science of building compiler, Applications of compiler technology, Programming language basics \n
        Lexical Analysis:\n
        The role of lexical analyzer, Input buffering, Specifications of token, recognition of tokens, lexical analyzer generator, Finite automate.""",'4':"""Module 4: 3D Viewing and Visible Surface Detection \n
        3D Viewing and Visible Surface Detection:
        3DViewing:3D viewing concepts, 3D viewing pipeline, 3D viewing coordinate parameters , Transformation fromworld to viewing coordinates, Projection transformation, orthogonal projections, perspective projections, The viewport transformation and 3D screen coordinates. OpenGL 3D viewing functions. Visible Surface Detection Methods: Classification of visible surface Detection algorithms, back face detection, depth buffer method and OpenGL visibility detection functions.""",'5':"""Module 5: Input& interaction, Curves and Computer Animation \n
        Input& interaction, Curves and Computer Animation:
        Input and Interaction: Input devices, clients and servers, Display Lists, Display Lists and Modelling, Programming Event Driven Input, Menus Picking, Building Interactive Models, Animating Interactive programs, Design of Interactive programs, Logic operations .Curved surfaces, quadric surfaces, OpenGL Quadric-Surface and Cubic-Surface Functions, Bezier Spline Curves, Bezier surfaces, OpenGL curve functions. Corresponding openGL functions."""
        },
        "os":{'1':"""MODULE 1:Introduction to operating systems, System structures: What operating systems
        do; Computer System organization; Computer System architecture; Operating
        System structure; Operating System operations; Process management; Memory
        management; Storage management; Protection and Security; Distributed system;
        Special-purpose systems; Computing environments. Operating System Services;
        User - Operating System interface; System calls; Types of system calls; System
        programs; Operating system design and implementation; Operating System
        structure; Virtual machines; Operating System generation; System boot. Process
        Management Process concept; Process scheduling; Operations on processes;
        Inter process communication
        """,'2':"""MODULE 2:Multi-threaded Programming: Overview; Multithreading models; Thread
        Libraries; Threading issues. Process Scheduling: Basic concepts; Scheduling
        Criteria; Scheduling Algorithms; Multiple-processor scheduling; Thread
        scheduling. Process Synchronization: Synchronization: The critical section
        problem; Peterson’s solution; Synchronization hardware; Semaphores; Classical
        problems of synchronization; Monitors. """,'3':"""MODULE 3:Deadlocks : Deadlocks; System model; Deadlock characterization; Methods for
        handling deadlocks; Deadlock prevention; Deadlock avoidance; Deadlock
        detection and recovery from deadlock. Memory Management: Memory
        management strategies: Background; Swapping; Contiguous memory allocation;
        Paging; Structure of page table; Segmentation. """,'4':"""MODULE 4:Virtual Memory Management: Background; Demand paging; Copy-on-write;
        Page replacement; Allocation of frames; Thrashing. File System,
        Implementation of File System: File system: File concept; Access methods;
        Directory structure; File system mounting; File sharing; Protection:
        Implementing File system: File system structure; File system implementation;
        Directory implementation; Allocation methods; Free space management. """,'5':"""MODULE 5:Secondary Storage Structures, Protection: Mass storage structures; Disk
        structure; Disk attachment; Disk scheduling; Disk management; Swap space
        management. Protection: Goals of protection, Principles of protection, Domain of
        protection, Access matrix, Implementation of access matrix, Access control,
        Revocation of access rights, Capability- Based systems. Case Study: The Linux
        Operating System: Linux history; Design principles; Kernel modules; Process
        management; Scheduling; Memory Management; File systems, Input and output;"""},
        "cg":{'1':"""MODULE 1:Overview: Computer Graphics and OpenGL: Computer Graphics:Basics of
        computer graphics, Application of Computer Graphics, Video Display Devices:
        Random Scan and Raster Scan displays, color CRT monitors, Flat panel displays.
        Raster-scan systems: video controller, raster scan Display processor, graphics
        workstations and viewing systems, Input devices, graphics networks, graphics on
        the internet, graphics software. OpenGL: Introduction to OpenGL ,coordinate
        reference frames, specifying two-dimensional world coordinate reference frames
        in OpenGL, OpenGL point functions, OpenGL line functions, point attributes,
        line attributes, curve attributes, OpenGL point attribute functions, OpenGL line
        attribute functions, Line drawing algorithms(DDA, Bresenham’s), circle
        generation algorithms(Bresenham’s).""",'2':"""MODULE 2:Fill area Primitives, 2D Geometric Transformations and 2D viewing: Fill
        area Primitives: Polygon fill-areas, OpenGL polygon fill area functions, fill area
        attributes, general scan line polygon fill algorithm, OpenGL fill-area attribute
        functions. 2DGeometric Transformations: Basic 2D Geometric Transformations,
        matrix representations and homogeneous coordinates. Inverse transformations,
        2DComposite transformations, other 2D transformations, raster methods for
        geometric transformations, OpenGL raster transformations, OpenGL geometric
        transformations function, 2D viewing: 2D viewing pipeline, OpenGL 2D viewing
        functions """,'3':"""MODULE 3:Clipping,3D Geometric Transformations, Color and Illumination Models:
        Clipping: clipping window, normalization and viewport transformations, clipping
        algorithms,2D point clipping, 2D line clipping algorithms: cohen-sutherland line
        clipping only -polygon fill area clipping: Sutherland-Hodgeman polygon clipping
        algorithm only.3DGeometric Transformations: 3D translation, rotation, scaling,
        composite 3D transformations, other 3D transformations, affine transformations,
        OpenGL geometric transformations functions. Color Models: Properties of light,
        color models, RGB and CMY color models. Illumination Models: Light sources,
        basic illumination models-Ambient light, diffuse reflection, specular and phong
        model, Corresponding openGL functions. """,'4':"""MODULE 4:3D Viewing and Visible Surface Detection: 3DViewing:3D viewing concepts,
        3D viewing pipeline, 3D viewing coordinate parameters , Transformation from
        10 Hours
        world to viewing coordinates, Projection transformation, orthogonal projections,
        perspective projections, The viewport transformation and 3D screen coordinates.
        OpenGL 3D viewing functions. Visible Surface Detection Methods:
        Classification of visible surface Detection algorithms, back face detection, depth
        buffer method and OpenGL visibility detection functions. 
        """,'5':"""MODULE 5:Input& interaction, Curves and Computer Animation: Input and Interaction:
        Input devices, clients and servers, Display Lists, Display Lists and Modelling,
        Programming Event Driven Input, Menus Picking, Building Interactive Models,
        Animating Interactive programs, Design of Interactive programs, Logic
        operations .Curved surfaces, quadric surfaces, OpenGL Quadric-Surface and
        Cubic-Surface Functions, Bezier Spline Curves, Bezier surfaces, OpenGL curve
        functions. Corresponding openGL functions. 
        """},
        "py":{'1':"""MODULE 1:Why should you learn to write programs, Variables, expressions and statements,
        Conditional execution, Functions """,'2':"""MODULE 2:Iteration, Strings, Files """,'3':"""MODULE 3:Lists, Dictionaries, Tuples, Regular Expressions """,'4':"""MODULE 4:Classes and objects, Classes and functions, Classes and methods""",'5':"""MODULE 5:Networked programs, Using Web Services, Using databases and SQL """}}
    modwise=syb[subject][module]
    print(modwise)
    return modwise