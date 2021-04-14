##############################################################################
# PURPOSE:
#    (This is a Python input file for configuring the Space Reference FOM
#     example early joiner federate run.)
#
# REFERENCE:
#    (Trick 17 documentation.)
#
# ASSUMPTIONS AND LIMITATIONS:
#    ((Uses the SpaceFOMFederateConfig Python class.)
#     (Uses the SpaceFOMRefFrameObject Python class.))
#
# PROGRAMMERS:
#    (((Edwin Z. Crues) (NASA/ER7) (Jan 2019) (--) (SpaceFOM support and testing.))
#     ((Dan Dexter) (NASA/ER6) (Aug 2020) (--) (Updated command-line parsing.))))
##############################################################################
import sys
sys.path.append('../../../')
# Load the SpaceFOM specific federate configuration object.
from Modified_data.SpaceFOM.SpaceFOMFederateConfig import *
# Load the SpaceFOM specific reference frame configuration object.
from Modified_data.SpaceFOM.SpaceFOMRefFrameObject import *

#---------------------------------------------------------------------------
# Command line usage and parsing.
#---------------------------------------------------------------------------
def print_usage_message( ) :

   print(' ')
   print('TrickHLA SpaceFOM Other Simulation Command Line Configuration Options:')
   print('  -h -help                : Print this help message.')
   print('  -blocking-reads [on|off]: on: Turns on blocking cyclic reads, off: disables it (Default).')
   print('  -realtime [on|off]      : on: Turns on realtime clock, off: disables it (Default).')
   print('  -hla-time-mgt [on|off]  : on: Turns on HLA Time Management (Default), off: disables it.')
   print('  -regulating [on|off]    : on: Turns on HLA Time Regulating, off: disables it (Default).')
   print('  -constrained [on|off]   : on: Turns on HLA Time Constrained (Default), off: disables it.')
   print('  -stop [time]            : Time to stop simulation, default is 10.0 seconds.')
   print('  -nostop                 : Set no stop time on simulation.')
   print('  -verbose [on|off]       : on: Show verbose messages, off: disable messages (Default).')
   print(' ')
   
   trick.exec_terminate_with_return( -1,
                                     sys._getframe(0).f_code.co_filename,
                                     sys._getframe(0).f_lineno,
                                     'Print usage message.')
   return

def parse_command_line( ) :
   
   global print_usage
   global blocking_reads
   global realtime_clock
   global hla_time_mgt
   global time_regulating
   global time_constrained
   global run_duration
   global verbose
   
   # Get the Trick command line arguments.
   argc = trick.command_line_args_get_argc()
   argv = trick.command_line_args_get_argv()
   
   # Process the command line arguments.
   # argv[0]=S_main*.exe, argv[1]=RUN/input.py file
   index = 2
   while (index < argc) :
      
      if (str(argv[index]) == '-blocking-reads') :
         index = index + 1
         if (index < argc) :
            if (str(argv[index]) == 'on') :
               blocking_reads = True
            elif (str(argv[index]) == 'off') :
               blocking_reads = False
            else :
               print('ERROR: Unknown -blocking-reads argument: ' + str(argv[index]))
               print_usage = True
         else :
            print('ERROR: Missing -blocking-reads [on|off] argument.')
            print_usage = True
            
      elif (str(argv[index]) == '-realtime') :
         index = index + 1
         realtime_clock
         if (index < argc) :
            if (str(argv[index]) == 'on') :
               realtime_clock = True
            elif (str(argv[index]) == 'off') :
               realtime_clock = False
            else :
               print('ERROR: Unknown -realtime argument: ' + str(argv[index]))
               print_usage = True
         else :
            print('ERROR: Missing -realtime [on|off] argument.')
            print_usage = True
            
      elif (str(argv[index]) == '-hla-time-mgt') :
         index = index + 1
         if (index < argc) :
            if (str(argv[index]) == 'on') :
               hla_time_mgt = True
            elif (str(argv[index]) == 'off') :
               hla_time_mgt = False
            else :
               print('ERROR: Unknown -hla-time-mgt argument: ' + str(argv[index]))
               print_usage = True
         else :
            print('ERROR: Missing -hla-time-mgt [on|off] argument.')
            print_usage = True
            
      elif (str(argv[index]) == '-regulating') :
         index = index + 1
         if (index < argc) :
            if (str(argv[index]) == 'on') :
               time_regulating = True
            elif (str(argv[index]) == 'off') :
               time_regulating = False
            else :
               print('ERROR: Unknown -regulating argument: ' + str(argv[index]))
               print_usage = True
         else :
            print('ERROR: Missing -regulating [on|off] argument.')
            print_usage = True
            
      elif (str(argv[index]) == '-constrained') :
         index = index + 1
         if (index < argc) :
            if (str(argv[index]) == 'on') :
               time_constrained = True
            elif (str(argv[index]) == 'off') :
               time_constrained = False
            else :
               print('ERROR: Unknown -constrained argument: ' + str(argv[index]))
               print_usage = True
         else :
            print('ERROR: Missing -constrained [on|off] argument.')
            print_usage = True
            
      elif (str(argv[index]) == '-stop') :
         index = index + 1
         if (index < argc) :
            run_duration = float(str(argv[index]))
         else :
            print('ERROR: Missing -stop [time] argument.')
            print_usage = True
            
      elif (str(argv[index]) == '-nostop') :
         run_duration = None
         
      elif ((str(argv[index]) == '-h') | (str(argv[index]) == '-help')) :
         print_usage = True
      
      elif (str(argv[index]) == '-verbose') :
         index = index + 1
         if (index < argc) :
            if (str(argv[index]) == 'on') :
               verbose = True
            elif (str(argv[index]) == 'off') :
               verbose = False
            else :
               print('ERROR: Unknown -verbose argument: ' + str(argv[index]))
               print_usage = True
         else :
            print('ERROR: Missing -verbose [on|off] argument.')
            print_usage = True
      
      else :
         print('ERROR: Unknown command line argument ' + str(argv[index]))
         print_usage = True
    
      index = index + 1
   return


# Default: Don't print the usage.
print_usage = False

# Default: Use blocking cyclic data reads.
blocking_reads = False

# Default: Disable realtime clock.
realtime_clock = False

# Default: Use HLA time management.
hla_time_mgt = True

# Default: Not Time-Regulating
time_regulating = False

# Default: Time-Constrained
time_constrained = True

# Default run duration.
run_duration = 10.0

# Default no verbose messages.
verbose = False

parse_command_line()

if (print_usage == True) :
   print_usage_message()


#---------------------------------------------
# Set up Trick executive parameters.
#---------------------------------------------
#instruments.echo_jobs.echo_jobs_on()
trick.exec_set_trap_sigfpe(True)
#trick.checkpoint_pre_init(1)
#trick.checkpoint_post_init(1)
#trick.add_read(0.0 , '''trick.checkpoint('chkpnt_point')''')

# Setup for Trick real time execution. This is the "Pacing" function.
if (realtime_clock == True) :   
   print('Realtime Clock Enabled.')
   exec(open( "Modified_data/trick/realtime.py" ).read())
else :
   print('Realtime Clock Disabled.')

trick.exec_set_enable_freeze(False)
trick.exec_set_freeze_command(False)
trick.sim_control_panel_set_enabled(False)
trick.exec_set_stack_trace(False)

# Log the elapsed-time between cyclic data reads.
exec(open( "Modified_data/elapsed_time.dr" ).read())


# =========================================================================
# Set up the HLA interfaces.
# =========================================================================
# Instantiate the Python SpaceFOM configuration object.
federate = SpaceFOMFederateConfig( THLA.federate,
                                   THLA.manager,
                                   THLA.execution_control,
                                   THLA.ExCO,
                                   'SpaceFOM_Roles_Test',
                                   'Other',
                                   True )

# Set the name of the ExCO S_define instance.
# We do not need to do this since we're using the ExCO default_data job
# to configure the ExCO. This is only needed for input file configuration.
#federate.set_ExCO_S_define_name( 'THLA_INIT.ExCO' )

# Set the debug output level.
if (verbose == True) : 
   federate.set_debug_level( trick.TrickHLA.DEBUG_LEVEL_4_TRACE )
else :
   federate.set_debug_level( trick.TrickHLA.DEBUG_LEVEL_0_TRACE )

#--------------------------------------------------------------------------
# Configure this federate SpaceFOM roles for this federate.
#--------------------------------------------------------------------------
federate.set_master_role( False ) # This is NOT the Master federate.
federate.set_pacing_role( False ) # This is NOT the Pacing federate.
federate.set_RRFP_role( False )   # This is NOT the Root Reference Frame Publisher.

#--------------------------------------------------------------------------
# Add in known required federates.
#--------------------------------------------------------------------------
# This is the RRFP federate.
# It doesn't really need to know about any other federates.
federate.add_known_fededrate( True, str(federate.federate.name) )
federate.add_known_fededrate( True, 'Master' )
federate.add_known_fededrate( True, 'Pacing' )
federate.add_known_fededrate( True, 'RRFP' )

#--------------------------------------------------------------------------
# Configure the CRC.
#--------------------------------------------------------------------------
# Pitch specific local settings designator:
THLA.federate.local_settings = 'crcHost = localhost\n crcPort = 8989'
#THLA.federate.local_settings = 'crcHost = 10.8.0.161\n crcPort = 8989'
# Mak specific local settings designator, which is anything from the rid.mtl file:
#THLA.federate.local_settings = '(setqb RTI_tcpForwarderAddr \'192.168.15.3\') (setqb RTI_distributedForwarderPort 5000)'

#--------------------------------------------------------------------------
# Set up federate related time related parameters.
#--------------------------------------------------------------------------
# Must specify a federate HLA lookahead value in seconds.
federate.set_lookahead_time( 0.250 )


# Setup Time Management parameters.
if (hla_time_mgt == False) :
   print('HLA Time Management Disabled.')
   federate.set_time_management( False )
else :
   print('HLA Time Management Enabled.')
   # True to enable TAR/TAG/Regulating/Constrained HLA API's
   federate.set_time_management( True )
   
   if (time_regulating == False) :
      print('HLA Time Regulating Disabled.')
      federate.set_time_regulating( False )
   else :
      print('HLA Time Regulating Enabled.')
      federate.set_time_regulating( True )
   
   if (time_constrained == False) :
      print('HLA Time Constrained Disabled.')
      federate.set_time_constrained( False )
   else :
      print('HLA Time Constrained Enabled.')
      federate.set_time_constrained( True )


#--------------------------------------------------------------------------
# Set up CTE time line.
#--------------------------------------------------------------------------
# By setting this we are specifying the use of Common Timing Equipment (CTE)
# for controlling the Mode Transitions for all federates using CTE.
# Don't really need CTE for RRFP.
#THLA.execution_control.cte_timeline = trick.sim_services.alloc_type( 1, 'TrickHLA::CTETimelineBase' )


#---------------------------------------------------------------------------
# Set up the Root Reference Frame object for discovery.
# If it is the RRFP, it will publish the frame.
# If it is NOT the RRFP, it will subscribe to the frame.
#---------------------------------------------------------------------------
root_frame = SpaceFOMRefFrameObject( federate.is_RRFP,
                                     'RootFrame',
                                     root_ref_frame.frame_packing,
                                     'root_ref_frame.frame_packing' )

# Set the debug flag for the root reference frame.
root_ref_frame.frame_packing.debug = verbose

# Blocking cyclic reads.
if (blocking_reads == True) :
   print('Blocking cyclic reads for RootFrame Enabled.')
   root_frame.set_blocking_cyclic_read( True )
else :
   print('Blocking cyclic reads for RootFrame Disabled.')
   root_frame.set_blocking_cyclic_read( False )

# Set the root frame for the federate.
federate.set_root_frame( root_frame )

#---------------------------------------------------------------------------
# Set up the Root Reference Frame object for discovery.
# If it is the RRFP, it will publish the frame.
# If it is NOT the RRFP, it will subscribe to the frame.
#---------------------------------------------------------------------------
frame_A = SpaceFOMRefFrameObject( False,
                                  'FrameA',
                                  ref_frame_A.frame_packing,
                                  'ref_frame_A.frame_packing' )

# Set the debug flag for the root reference frame.
ref_frame_A.frame_packing.debug = verbose

# Blocking cyclic reads.
if (blocking_reads == True) :
   print('Blocking cyclic reads for FrameA Enabled.')
   frame_A.set_blocking_cyclic_read( True )
else :
   print('Blocking cyclic reads for FrameA Disabled.')
   frame_A.set_blocking_cyclic_read( False )

# Add this reference frame to the list of managed object.
federate.add_fed_object( frame_A )

#---------------------------------------------------------------------------
# Add the HLA SimObjects associated with this federate.
# This is really only useful for turning on and off HLA objects.
# This doesn't really apply to these example simulations which are only HLA.
#---------------------------------------------------------------------------
federate.add_sim_object( THLA )
federate.add_sim_object( THLA_INIT )
federate.add_sim_object( root_ref_frame )
federate.add_sim_object( ref_frame_A )


#---------------------------------------------------------------------------
# Make sure that the Python federate configuration object is initialized.
#---------------------------------------------------------------------------
#federate.disable()
federate.initialize()


#---------------------------------------------------------------------------
# Set up simulation termination time.
#---------------------------------------------------------------------------
if run_duration:
   print('Run duration: ' + str(run_duration))
   trick.sim_services.exec_set_terminate_time( run_duration )


#---------------------------------------------------------------------------
# Send a timed MTR request to the Master federate.
#---------------------------------------------------------------------------
# Send an interaction.
#trick.add_read(3.0 , """THLA.manager.send_MTR_interation( trick.SpaceFOM.MTR_GOTO_SHUTDOWN )""")
#trick.add_read(3.0 , """THLA.manager.send_MTR_interation( trick.SpaceFOM.MTR_GOTO_FREEZE )""")
